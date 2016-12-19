import re

file = open('Day 4 input.txt', 'r')
inp = file.read()


def num_to_char(num):
    return chr(num + ord('a') - 1)


def char_to_num(char):
    return ord(char.lower()) - ord('a') + 1


class Room(object):
    def __init__(self, encrypt):
        self.encrypt = encrypt
        p = re.compile('(\D+)\-(\d+)\[(.+)\]')
        m = p.match(encrypt)

        self.name = m.group(1)
        self.sector = int(m.group(2))
        self.checksum = m.group(3)

    def frequencies(self):
        letter_count = []
        temp = self.name.replace("-", "")

        #count letter occurrences
        while temp != "":
            c = temp[0]
            letter_count.append((c, temp.count(c)))
            temp = temp.replace(c, "")

        #sort list; first alphabetically, then by count
        letter_count.sort(key=lambda x: x[0])
        letter_count.sort(key=lambda x: x[1], reverse=True)

        return letter_count

    def real(self):
        check = ""

        #find 5 most common letters
        for i in range(5):
            check += self.frequencies()[i][0]

        if check == self.checksum:
            return True
        else:
            return False

    def cipher_name(self):
        final = ""
        for c in self.name:
            if c == "-":
                final += " "
            else:
                v = char_to_num(c)
                v += self.sector
                v = (v - 1) % 26 + 1
                final += num_to_char(v)

        return final

sector_sum = 0
sector_id = 0

for line in inp.split('\n'):
    r = Room(line)
    if r.real():
        sector_sum += r.sector
        #search for string containing 'object'
        if "object" in r.cipher_name():
            sector_id = r.sector

print('1st answer: ' + str(sector_sum))
print('2nd answer: ' + str(sector_id))