import re
import itertools
import collections

file = open('Day 11 input.txt', 'r')
inp = file.read()


class Metal(object):
    def __init__(self, generator_floor=1, microchip_floor=1):
        self.generator_floor = generator_floor
        self.microchip_floor = microchip_floor

    def protected(self):
        return self.generator_floor == self.microchip_floor

    def copy(self):
        m = Metal()
        m.generator_floor = self.generator_floor
        m.microchip_floor = self.microchip_floor
        return m


class State(object):
    def __init__(self, floors):
        self.metals = collections.defaultdict(Metal)
        self.elevator = 1
        self.floors = floors

    def __hash__(self):
        return hash(self.string())

    def __eq__(self, other):
        return self.string() == other.string()

    #boolean whether valid state
    def valid(self):
        #flag which floors have generators
        gen = {x:False for x in range(1, self.floors + 1)}
        for m in self.metals.values():
            gen[m.generator_floor] = True
        return all(m.protected() or not gen[m.microchip_floor] for m in self.metals.values())

    #boolean whether valid state
    def complete(self):
        return all(v.generator_floor == self.floors and v.microchip_floor == self.floors for v in self.metals.values())

    def copy(self):
        sc = State(self.floors)
        sc.elevator = self.elevator
        for k, m in self.metals.items():
            sc.metals[k] = m.copy()
        return sc

    def move(self, metal, generator=True, step=1):
        if generator:
            self.metals[metal].generator_floor += step
        else:
            self.metals[metal].microchip_floor += step

    #possible moves
    def poss_moves(self):
        ret = set()
        movable = [(k, True) for k, v in self.metals.items() if v.generator_floor == self.elevator] + \
                  [(k, False) for k, v in self.metals.items() if v.microchip_floor == self.elevator]
        steps = [s for s in [-1, 1] if 1 <= self.elevator + s <= self.floors]

        #construct list combinations for 1 and 2 items
        combs = []
        for i in [1, 2]:
            els = [list(x) for x in itertools.combinations(movable, i)]
            combs.extend(els)

        for s in steps:
            for p in combs:
                c = self.copy()
                for i in p:
                    c.move(i[0], i[1], s)
                c.elevator += s
                if c.valid():
                    ret.add(c.copy())

        return ret

    #identity of state
    #name of metals is unimportant, simply the configuration
    #count pairs (generator_floor, microchip_floor), list counts and elevator as identity
    def string(self):
        ret = 'E=' + str(self.elevator)
        encode = {key: 0 for key in itertools.product(range(1, 5), repeat=2)}

        for m in self.metals.values():
            encode[(m.generator_floor, m.microchip_floor)] += 1

        ret += '|I=' + ','.join([str(encode[k]) for k in sorted(encode.keys())])
        return ret


class Building(object):
    def __init__(self, start_state):
        self.start_state = start_state.copy()

    def moves(self):
        ret = 0
        prev_state_strings = set()
        last_states = set()
        last_states.add(self.start_state)

        while 1:
            ret += 1

            prev_state_strings.update(s.string() for s in last_states)
            new_states = set()

            for state in last_states:
                for move in state.poss_moves():
                    #once complete, return number of moves
                    if move.complete():
                        return ret
                    #ensure not already visited
                    if move.string() not in prev_state_strings:
                        new_states.add(move)

            last_states = new_states


ss = State(4)

#initialize start state
for i, line in enumerate(inp.split('\n'), 1):
    for s in line.split(' a '):
        m = re.match(r'(\w+).+', s)
        metal = m.group(1)[:2]
        if 'generator' in s:
            ss.metals[metal].generator_floor = i
        elif 'microchip' in s:
            ss.metals[metal].microchip_floor = i

b1 = Building(ss)

ss.metals['el'] = Metal(1, 1)
ss.metals['di'] = Metal(1, 1)

b2 = Building(ss)

print('1st answer: ' + str(b1.moves()))
print('2nd answer: ' + str(b2.moves()))
