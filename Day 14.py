import hashlib

inp = 'ahsbgdzn'
n = 64

def triplet(string):
    for i in range(len(string) - 2):
        if string[i] == string[i + 1] == string[i + 2]:
            return string[i]


def contains_quintuplet(string, c):
    return c * 5 in string


def key_hash(salt, i, iterations):
    s = salt + str(i)
    for x in range(iterations):
        m = hashlib.md5()
        m.update(s.encode('utf-8'))
        s = m.hexdigest().lower()
    return s


def pad_keys(salt, iterations, n):
    i = 0
    candidates = {}
    ret = []
    end = -1

    while end == -1 or i <= end: #len(ret) < n:
        h = key_hash(salt, i, iterations)

        found_keys = []

        for k in list(candidates.keys()):
            if k > i - 1000:
                if contains_quintuplet(h, candidates[k]):
                    found_keys.append(k)
                    del candidates[k]
            else:
                del candidates[k]

        ret += found_keys

        if len(ret) < n:
            #keep addding candidates
            c = triplet(h)
            if c:
                candidates[i] = c
        elif end == -1:
            for k in list(candidates.keys()):
                if k > max(ret):
                    del candidates[k]
            end = max(candidates.keys()) + 1000

        i += 1

    ret.sort()
    return ret[:n]

k1 = pad_keys('ahsbgdzn', 1, n)
k2 = pad_keys('ahsbgdzn', 2017, n)

print('1st answer: {0}'.format(k1[n - 1]))
print('2nd answer: {0}'.format(k2[n - 1]))