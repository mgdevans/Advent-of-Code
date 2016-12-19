
inp = '11101000110010100'
size = 272
size = 35651584
ret = inp

while len(ret) < size:
    b = ret[::-1]
    b = b.replace('0', '2')
    b = b.replace('1', '0')
    b = b.replace('2', '1')
    ret += ('0' + b)

checksum = ret[:size]

while len(checksum) % 2 == 0:
    nc = ''
    for i in range(int(len(checksum)/2)):
        pair = checksum[i*2:(i + 1)*2]
        if pair == pair[::-1]:
            nc += '1'
        else:
            nc += '0'
    checksum = nc

print(checksum)