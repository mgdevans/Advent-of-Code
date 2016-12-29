tgl_map = {'cpy': 'jnz',
           'jnz': 'cpy',
           'inc': 'dec',
           'dec': 'inc',
           'tgl': 'inc'}


class Command(object):

    def __init__(self, cmd, args):
        self.cmd = cmd
        self.args = args
        self.location = 0

    def toggle(self):
        self.cmd = tgl_map[self.cmd]


class Computer(object):

    def __init__(self, registers, script):
        self.location = 0
        self.registers = registers
        self.commands = []
        for line in script.split('\n'):
            vals = line.split(' ')
            args = [s if s in self.registers.keys() else int(s) for s in vals[1:]]
            cmd = vals[0]
            self.commands.append(Command(cmd, args))

    def value(self, arg):
        if arg in self.registers.keys():
            return self.registers[arg]
        else:
            return arg

    def step(self):

        loc = self.location

        #spot multiplication
        if ''.join(x.cmd for x in self.commands[loc:loc+6]) == 'cpyincdecjnzdecjnz':
            if all(x.args[0] in self.registers.keys() for x in self.commands[loc+1:loc+6]) and self.commands[loc + 3].args[1] == -2 and self.commands[loc + 5].args[1] == -5:
                self.registers[self.commands[loc + 1].args[0]] += self.value(self.commands[loc].args[0]) * self.registers[self.commands[loc + 4].args[0]]
                self.registers[self.commands[loc + 4].args[0]] = 0
                self.registers[self.commands[loc + 2].args[0]] = 0
                self.location += 6
                return

        #spot addition/subtraction
        if ''.join(x.cmd for x in self.commands[loc:loc+3]) in ['incincjnz', 'incdecjnz', 'decincjnz', 'decdecjnz']:
            if self.commands[loc + 2].args[0] in self.registers.keys() and self.commands[loc + 2].args[1] == -2:
                r = self.commands[loc + 2].args[0]
                for c in self.commands[loc:loc+2]:
                    if c.args[0] != self.commands[loc + 2].args[0]:
                        if c.cmd == 'dec':
                            self.registers[c.args[0]] += abs(self.registers[r])
                        else:
                            self.registers[c.args[0]] += abs(self.registers[r])
                self.registers[r] = 0
                self.location += 3
                return

        #else usual commands
        shift = 1
        c = self.commands[loc]

        if c.cmd == 'cpy' and c.args[1] in self.registers.keys():
            self.registers[c.args[1]] = self.value(c.args[0])

        elif c.cmd == 'inc':
            self.registers[c.args[0]] += 1

        elif c.cmd == 'dec':
            self.registers[c.args[0]] -= 1

        elif c.cmd == 'jnz':
            if self.value(c.args[0]) != 0:
                shift = self.value(c.args[1])

        elif c.cmd == 'tgl':
            index = loc + self.value(c.args[0])
            if 0 <= index < len(self.commands):
                self.commands[index].cmd = tgl_map[self.commands[index].cmd]

        self.location += shift

    def process(self):

        while 0 <= self.location < len(self.commands):
            self.step()

