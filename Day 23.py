import Assembunny

file = open('Day 23 input.txt', 'r')
inp = file.read()

c1 = Assembunny.Computer({'a': 7, 'b': 0, 'c': 0, 'd': 0}, inp)
c2 = Assembunny.Computer({'a': 12, 'b': 0, 'c': 1, 'd': 0}, inp)

c1.process()
c2.process()

print('1st answer: {}'.format(c1.registers['a']))
print('2nd answer: {}'.format(c2.registers['a']))
