file = open('Day 6 input.txt', 'r')
inp = file.read()

lines = inp.split('\n')
msg1 = ""
msg2 = ""

#Loop over columns
for i in range(len(lines[0])):
    col = ""

    #loop over rows, create column string
    for line in lines:
        col += line[i]

    letter_count = []

    #count letter occurrences
    while col != "":
        c = col[0]
        letter_count.append((c, col.count(c)))
        col = col.replace(c, "")

    letter_count.sort(key=lambda x: x[1])

    msg1 += letter_count[-1][0]
    msg2 += letter_count[0][0]

print('1st answer: ' + msg1)
print('2nd answer: ' + msg2)
