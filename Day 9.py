import re

file = open('Day 9 input.txt', 'r')
inp = file.read()


def dec_length(string, nested):
    p = re.compile(r'(.*?)\((\d+)x(\d+)\)(.*)')
    m = p.match(string)

    if m:

        start = m.group(1)
        length = int(m.group(2))
        repeat = int(m.group(3))
        end = m.group(4)

        #if nested calculate decompressed length of repetition
        if nested:
            nest = dec_length(end[:length], nested)
        else:
            nest = length

        return len(start) + repeat * nest + dec_length(end[length:], nested)

    else:
        return len(string)

print('1st answer: ' + str(dec_length(inp, False)))
print('2nd answer: ' + str(dec_length(inp, True)))