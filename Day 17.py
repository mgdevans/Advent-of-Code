import hashlib

width = 4
height = 4
valid = {'b', 'c', 'd', 'e', 'f'}

class Path(object):
    def __init__(self):
        self.passcode = ''
        self.string = ''
        self.x = 1
        self.y = 1

    def copy(self):
        pc = Path()
        pc.passcode = self.passcode
        pc.string = self.string
        pc.x = self.x
        pc.y = self.y
        return pc

    def possible_paths(self):
        ret = set()
        m = hashlib.md5()
        m.update((self.passcode + self.string).encode('utf-8'))
        h = m.hexdigest().lower()

        if self.y > 1 and h[0] in valid:
            p = self.copy()
            p.y -= 1
            p.string += 'U'
            ret.add(p)

        if self.y < width and h[1] in valid:
            p = self.copy()
            p.y += 1
            p.string += 'D'
            ret.add(p)

        if self.x > 1 and h[2] in valid:
            p = self.copy()
            p.x -= 1
            p.string += 'L'
            ret.add(p)

        if self.x < height and h[3] in valid:
            p = self.copy()
            p.x += 1
            p.string += 'R'
            ret.add(p)

        return ret


start = Path()
start.passcode = 'qljzarfv'

paths = set()
paths.add(start)

solutions = set()
ans1 = ''

while len(paths) != 0:
    new_paths = set()
    for p in paths:
        if p.x == width and p.y == height:
            if ans1 == '':
                ans1 = p.string
            solutions.add(p)
        else:
            new_paths.update(p.possible_paths())
    paths = new_paths.copy()

ans2 = max([len(s.string) for s in solutions])

print('1st answer: {0}'.format(ans1))
print('2nd answer: {0}'.format(ans2))