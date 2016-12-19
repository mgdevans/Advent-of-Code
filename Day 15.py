file = open('Day 15 input.txt', 'r')
inp = file.read()


class Disc(object):
    def __init__(self):
        self.positions = 1
        self.state = 0

    def tick(self, number=1):
        self.state = (self.state + number) % self.positions


class Sculpture(object):
    def __init__(self):
        self.discs = []
        self.time = 0

    def add_disc(self, positions, state):
        d = Disc()
        d.positions = positions
        d.state = state
        self.discs.append(d)

    def capsule_time(self):
        #offset each disc by position
        for i, d in enumerate(self.discs, 1):
            d.tick(i)

        #loop until find alignment
        while 1:
            if all(d.state == 0 for d in self.discs):
                break
            self.time += 1
            for d in self.discs:
                d.tick()

        return self.time

d1 = Sculpture()
d2 = Sculpture()

for i, line in enumerate(inp.split('\n'), 1):
    words = line.split(' ')

    p = int(words[3])
    s = int(words[11].replace('.', ''))

    d1.add_disc(p, s)
    d2.add_disc(p, s)

d2.add_disc(11, 0)

print('1st answer: ' + str(d1.capsule_time()))
print('2nd answer: ' + str(d2.capsule_time()))

