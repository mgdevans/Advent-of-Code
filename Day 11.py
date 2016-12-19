import re

file = open('Day 11 input.txt', 'r')
inp = file.read()


class Floor(object):
    def __init__(self):
        self.generators = set()
        self.microchips = set()

    def contents(self):
         return 'M={' + ', '.join(sorted(self.generators)) + \
                '}, G={' + ', '.join(sorted(self.microchips)) + '}'


class Move(object):
    def __init__(self):
        self.up = False
        self.generator = False
        self.metal = ''

    def val(self):
        return  'up=' + str(self.up) + \
                ',generator=' + str(self.generator) + \
                ',metal=' + self.metal

class Building(object):
    def __init__(self):
        self.floors = {}
        self.elevator = 1
        self.states = set()

    #state of all elements
    def state(self):
        ret = 'E=' + str(self.elevator)
        for key in sorted(self.floors.keys()):
            ret += ', F' + str(key) + '={' + self.floors[key].contents() + '}'
        return ret

    #moves item
    def move(self, move):
        #save state before move
        self.states.add(self.state())

        if move.up:
            next_floor = self.elevator + 1
        else:
            next_floor = self.elevator + 1

        if move.generator:
            self.floors[self.elevator].generators.remove(move.metal)
            self.floors[next_floor].generators.add(move.metal)
        else:
            self.floors[self.elevator].microchips.remove(move.metal)
            self.floors[next_floor].microchips.add(move.metal)

        self.elevator = next_floor

    #possible moves
    def poss_moves(self):
        ret = set()
        m = Move()
        for u in [True, False]:
            if u
            for g in self.floors[self.elevator].generators:



    #boolean whether been to state previously
    def loop(self):
        if self.state() in self.states:
            return False
        else:
            return True


B = Building()

for i, line in enumerate(inp.split('\n'), 1):
    B.floors[i] = Floor()
    for s in line.split(' a '):
        m = re.match(r'(\w+).+', s)
        metal = m.group(1)[:2]
        if 'generator' in s:
            B.floors[i].generators.add(metal)
        elif 'microchip' in s:
            B.floors[i].microchips.add(metal)
    print(B.floors[i].contents())




