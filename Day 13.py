class Location(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def shift(self, x, y):
        self.x += x
        self.y += y

    def wall(self):
        n = self.x*self.x + 3*self.x + 2*self.x*self.y + self.y + self.y*self.y + 1358
        return "{0:b}".format(n).count('1') % 2 == 1

    def possible_moves(self):
        places = set()
        steps = [[0, 1], [1, 0]]
        if self.x != 0:
            steps.append([-1, 0])
        if self.y != 0:
            steps.append([0, -1])

        for s in steps:
            l = Location(self.x, self.y)
            l.shift(s[0], s[1])
            if not l.wall():
                places.add(l)

        return places

goal = Location(31, 39)

#create dictionary of sets of places
#the key is the number of steps it takes to get there
initial = set()
initial.add(Location(1, 1))
found = {0: initial}
steps = 0

while goal not in found[steps]:
    new_places = set()

    for f in found[steps]:
        for p in f.possible_moves():
            if all(p not in s for s in found.values()):
                new_places.add(p)

    steps += 1
    found[steps] = new_places

ans2 = 0

for k, s in found.items():
    if k <= 50:
        ans2 += len(s)

print('1st answer: {0}'.format(steps))
print('2nd answer: {0}'.format(ans2))