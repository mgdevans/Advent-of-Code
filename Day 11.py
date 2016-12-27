import re
import itertools

file = open('Day 11 input.txt', 'r')
inp = file.read()


class Item(object):
    def __init__(self):
        self.generator = False
        self.metal = ''


class Floor(object):
    def __init__(self):
        self.generators = set()
        self.microchips = set()

    #check floor doesn't fry any chips
    def valid(self):
        #check chip paired OR ensure no generators
        return all(m in self.generators or not self.generators for m in self.microchips)

    def items(self):
        ret = []
        for g in self.generators:
            i = Item()
            i.generator = True
            i.metal = g
            ret.append(i)
        for m in self.microchips:
            i = Item()
            i.generator = False
            i.metal = m
            ret.append(i)
        return ret

    def copy(self):
        fc = Floor()
        fc.generators = self.generators.copy()
        fc.microchips = self.microchips.copy()
        return fc

    def empty(self):
        if self.generators or self.microchips:
            return False
        return True

class State(object):
    def __init__(self):
        self.floors = {}
        self.elevator = 1

    def __hash__(self):
        return hash(self.string())

    def __eq__(self, other):
        return self.string() == other.string()

    #boolean whether valid state
    def valid(self):
        #check all floors valid
        return all(f.valid() for f in self.floors.values())

    def move(self, item, destination):
        if item.generator:
            self.floors[self.elevator].generators.remove(item.metal)
            self.floors[destination].generators.add(item.metal)
        else:
            self.floors[self.elevator].microchips.remove(item.metal)
            self.floors[destination].microchips.add(item.metal)

    def copy(self):
        sc = State()
        sc.elevator = self.elevator
        for k, f in self.floors.items():
            sc.floors[k] = f.copy()
        return sc

    #possible moves
    def poss_moves(self):
        ret = set()
        movable = self.floors[self.elevator].items()
        destinations = [d for d in self.floors.keys() if d in [self.elevator + 1, self.elevator - 1]]

        #construct list combinations for 1 and 2 items
        combs = []
        for i in [1, 2]:
            els = [list(x) for x in itertools.combinations(movable, i)]
            combs.extend(els)

        for d in destinations:
            for p in combs:
                c = self.copy()
                for i in p:
                    c.move(i, d)
                c.elevator = d
                if c.valid():
                    ret.add(c.copy())

        return ret

    def complete(self):
        return all(self.floors[x].empty() for x in range(1, 4))

    #values of all elements
    def string(self):
        ret = 'E=' + str(self.elevator)
        encode = {key: 0 for key in itertools.product(range(1, 5), repeat=2)}
        metals = {}

        for k, f in self.floors.items():
            for m in f.microchips:
                metals[m] = k

        for k, f in self.floors.items():
            for g in f.generators:
                encode[(metals[g], k)] += 1

        ret += ',I=' + ''.join([str(encode[k]) for k in sorted(encode.keys())])
        return ret


class Building(object):
    def __init__(self, start_state):
        self.prev_state_strings = set()

        self.last_states = set()
        self.last_states.add(start_state.copy())
        self.moves = 0
        self.complete = False

    def next_move(self):
        self.moves += 1
        self.prev_state_strings.update(s.string() for s in self.last_states)
        new_states = set()

        for state in self.last_states:
            for move in state.poss_moves():
                if move.complete():
                    self.complete = True
                #check not already visited
                if move.string() not in self.prev_state_strings:
                    new_states.add(move)

        self.last_states = new_states

    def process(self):
        while not self.complete:
            self.next_move()


ss = State()

for i, line in enumerate(inp.split('\n'), 1):
    ss.floors[i] = Floor()
    for s in line.split(' a '):
        m = re.match(r'(\w+).+', s)
        metal = m.group(1)[:2]
        if 'generator' in s:
            ss.floors[i].generators.add(metal)
        elif 'microchip' in s:
            ss.floors[i].microchips.add(metal)

b1 = Building(ss)
b1.process()

ss.floors[1].generators.update(['el', 'di'])
ss.floors[1].microchips.update(['el', 'di'])

b2 = Building(ss)
b2.process()

print('1st answer: ' + str(b1.moves))
print('2nd answer: ' + str(b2.moves))