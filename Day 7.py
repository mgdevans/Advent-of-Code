import re
import itertools

file = open('Day 7 input.txt', 'r')
inp = file.read()
count1 = 0
count2 = 0


def abba(string):
    for i in range(len(string)-3):
        sub = string[i:i + 4]
        if sub[0] != sub[1] and sub == sub[::-1]:
            return True
    return False


def aba(string):
    if string[0] == string[2] and string[0] != string[1]:
        return True
    else:
        return False


def tls(string):
    i = 0
    ind = False

    for string in re.split('\W+', string):
        if abba(string):
            if i == 0:
                ind = True
            else:
                return False

        i = (i + 1) % 2

    return ind


def ssl(string):
    i = 0
    ind = False
    super_aba = set()
    hyper_aba = set()

    #collect ABA strings
    for string in re.split('\W+', string):
        for j in range(len(string)-2):
            sub = string[j:j + 3]
            if aba(sub):
                if i == 0:
                    super_aba.add(sub)
                else:
                    hyper_aba.add(sub)

        i = (i + 1) % 2

    #See if there is a super ABA = hyper BAB
    for sup, hyp in itertools.product(super_aba, hyper_aba):
        if sup[:2] == hyp[-2:]:
            ind = True
            break

    return ind


for line in inp.split('\n'):
    if tls(line):
        count1 += 1
    if ssl(line):
        count2 += 1


print('1st answer: ' + str(count1))
print('2nd answer: ' + str(count2))