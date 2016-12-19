import re
import collections

file = open('Day 10 input.txt', 'r')
inp = file.read()


class Location(object):
    def __init__(self):
        self.is_bot = True
        self.index = -1


class Bot(object):
    def __init__(self):
        self.chips = set()
        self.chips_recieved = set()
        self.high_location = Location()
        self.low_location = Location()

    def full(self):
        if len(self.chips) == 2:
            return True
        else:
            return False

    def low(self):
        ret = -1
        for c in self.chips:
            if ret == -1 or c < ret:
                ret = c
        return ret

    def high(self):
        ret = -1
        for c in self.chips:
            if ret == -1 or c > ret:
                ret = c
        return ret

    def update_chips(self):
        self.chips.update(self.chips_recieved)
        self.chips_recieved.clear()


#loop through initiation
bots = collections.defaultdict(Bot)
outputs = collections.defaultdict(set)

for line in inp.split('\n'):
    #send value chips to bots
    if line[:3] == 'val':
        m = re.match(r'.*?(\d+).*?(\d+)',line)
        v = int(m.group(1))
        b = int(m.group(2))

        bots[b].chips.add(v)

    #send instructions to bots
    else:
        m = re.match(r'.*?(\d+).*?to(.*?)(\d+).*?to(.*?)(\d+)',line)
        b = int(m.group(1))

        l_type = m.group(2)
        l_num = int(m.group(3))

        h_type = m.group(4)
        h_num = int(m.group(5))

        bots[b].low_location.is_bot = ('bot' in l_type)
        bots[b].low_location.index = l_num

        bots[b].high_location.is_bot = ('bot' in h_type)
        bots[b].high_location.index = h_num

        #ensure location bots exist
        for l in [bots[b].low_location, bots[b].high_location]:
            if l.is_bot:
                x = bots[l.index]


finished = False
answer1 = -1

while not finished:
    finished = True
    for k, b in bots.items():
        if b.full() == True:
            #if one bot is full, not finished
            finished = False

            #see if bot is comparing key values
            if b.low() == 17 and b.high() == 61:
                answer1 = k

            #complete exchange of chips
            for (ib, i, n) in [(b.low_location.is_bot, b.low_location.index, b.low()),
                               (b.high_location.is_bot, b.high_location.index, b.high())]:
                if ib:
                    bots[i].chips_recieved.add(n)
                else:
                    outputs[i].add(n)

            #remove chips from bot
            b.chips.clear()

    #update bots with all the recieved chips
    for k, b in bots.items():
        b.update_chips()

answer2 = 1

for i in range(3):
    for s in outputs[i]:
        answer2 *= s

print('1st answer: ' + str(answer1))
print('2nd answer: ' + str(answer2))