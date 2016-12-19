inp = 'R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1'
steps = inp.split(', ')


class Vector:
    def __init__(self):
        self.x = 0
        self.y = 0

    def tup(self):
        return tuple((self.x, self.y))


class Taxi(object):
    def __init__(self):
        self.location = Vector()
        self.direction = Vector()
        self.direction.y = 1

    def location(self):
        return self.location

    def turn(self, way):
        if way == 'R':
            self.direction.x, self.direction.y = self.direction.y, -self.direction.x
        else:
            self.direction.x, self.direction.y = -self.direction.y, self.direction.x

    def move(self,  blocks):
        self.location.x += self.direction.x * blocks
        self.location.y += self.direction.y * blocks

    def distance(self):
        return abs(self.location.x) + abs(self.location.y)

t = Taxi()
places = set([])
sec_found = False
sec_ans = 0

for step in steps:
    t.turn(step[:1])
    for b in range(0,int(step[1:])):
        places.add(t.location.tup())
        t.move(1)
        if (t.location.tup() in places) and (sec_found == False):
            sec_found = True
            sec_ans = t.distance()

print('1st answer: ' + str(t.distance()))
print('2nd answer: ' + str(sec_ans))
