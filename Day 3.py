file = open('Day 3 input.txt', 'r')
inp = file.read()


class Triangle(object):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def valid(self):
        if ((self.a + self.b > self.c) and
                (self.b + self.c > self.a) and
                (self.c + self.a > self.b)):
            return True
        else:
            return False

count1 = 0
count2 = 0

rows = [[int(s) for s in line.split()] for line in inp.split('\n')]

for i, row in enumerate(rows):
    c = i % 3
    r = i - c

    t1 = Triangle()
    t2 = Triangle()

    t1.a, t1.b, t1.c = row[0], row[1], row[2]
    t2.a, t2.b, t2.c = rows[r][c], rows[r + 1][c], rows[r + 2][c]

    if t1.valid():
        count1 += 1
    if t2.valid():
        count2 += 1


print('1st answer: ' + str(count1))
print('1st answer: ' + str(count2))