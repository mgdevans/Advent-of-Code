import re

file = open('Day 8 input.txt', 'r')
inp = file.read()

h = 6
w = 50
n = 5

class Screen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[0 for y in range(height)] for x in range(width)]

    def lit(self):
        return sum([sum(column) for column in self.pixels])

    def rect(self, x, y):
        for i in range(x):
            for j in range(y):
                self.pixels[i][j] = (self.pixels[i][j] + 1) % 2

    def column(self, x, y):
        self.pixels[x] = rotate(self.pixels[x], y)

    def row(self, x, y):
        temp_row = [column[y] for column in self.pixels]
        temp_row = rotate(temp_row, x)

        for i in range(self.width):
            self.pixels[i][y] = temp_row[i]

    def operation(self, command, x, y):
        if command == 'rect':
            self.rect(x, y)
        elif command == 'column':
            self.column(x, y)
        elif command == 'row':
            self.row(x, y)


def rotate(l, n):
    return l[-n:] + l[:-n]


s = Screen(50, 6)

for line in inp.split('\n'):
    line = line.replace('rotate ','')
    m = re.match('(\S+)\D+(\d+)\D+(\d+)', line)
    cmd = m.group(1)
    num1 = int(m.group(2))
    num2 = int(m.group(3))

    print(cmd + ": " + str(num1) + ", " + str(num2))

    if cmd == 'row':
        num1, num2 = num2, num1

    s.operation(cmd, num1, num2)

c = 'X'

print('1st answer: ' + str(s.lit()))
print('\n2nd answer:\n')
for j in range(h):
    row = [c if column[j] == 1 else ' ' for column in s.pixels]
    print("".join(row))


