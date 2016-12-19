file = open('Day 12 input.txt', 'r')
inp = file.read()

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
inst = [line.split(' ') for line in inp.split('\n')]


class Registers(object):
    def __init__(self, initial):
        self.values = initial

    def val(self, string):
        if string in registers.keys():
            return self.values[string]
        else:
            return int(string)

    def process(self):
        loc = 0

        while loc < len(inst):
            if inst[loc][0] == 'cpy':
                self.values[inst[loc][2]] = self.val(inst[loc][1])
                loc += 1
            elif inst[loc][0] == 'inc':
                self.values[inst[loc][1]] += 1
                loc += 1
            elif inst[loc][0] == 'dec':
                self.values[inst[loc][1]] -= 1
                loc += 1
            elif inst[loc][0] == 'jnz':
                if self.val(inst[loc][1]) == 0:
                    loc += 1
                else:
                    loc += int(inst[loc][2])


r1 = Registers({'a': 0, 'b': 0, 'c': 0, 'd': 0})
r2 = Registers({'a': 0, 'b': 0, 'c': 1, 'd': 0})

r1.process()
r2.process()

print('1st answer: ' + str(r1.values['a']))
print('2nd answer: ' + str(r2.values['a']))
