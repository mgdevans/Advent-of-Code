inp = 3014603

#define function for calculating first part
def f1(num):
    i = 1
    #find largest power of 2 less than num
    while i <= num:
        i *= 2
    i /= 2
    return int((num - i) * 2 + 1)

#iterate for 2nd part
#start at calculating 4th iteration, using 3rd
i = 4
f2 = 3 #for i = 3

while i <= inp:
    if f2 >= int(i/2):
        f2 += 1
    f2 = f2 % i + 1
    i += 1

print('1st answer: ' + str(f1(inp)))
print('2nd answer: ' + str(f2))
