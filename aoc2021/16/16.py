# https://adventofcode.com/2021/day/16

with open('in.in', 'r') as f:
    s = f.read().strip('\n')

stream = ''.join(list(map(lambda x: bin(int(x, 16))[2:].rjust(4, '0'), s)))
stream = list(stream)[::-1]
print(stream)


def getN(data_stream, n):
    res = []
    for i in range(n):
        res.append(data_stream.pop(-1))
    return ''.join(res)


all_versions = []


def decode(data_stream):
    v = getN(data_stream, 3)
    all_versions.append(int(v, 2))
    t = getN(data_stream, 3)
    t = int(t, 2)
    if t == 4:
        value = []
        while True:
            cnt, *v = getN(data_stream, 5)
            value.extend(v)
            if cnt == '0':
                break
        return int(''.join(value), 2)
    else:
        values = []
        i = getN(data_stream, 1)
        if i == '0':
            l = getN(data_stream, 15)
            l = int(l, 2)
            subpacket = getN(data_stream, l)
            subpacket = [v for v in subpacket][::-1]
            while subpacket:
                values.append(decode(subpacket))
        else:
            l = getN(data_stream, 11)
            l = int(l, 2)
            for i in range(l):
                values.append(decode(data_stream))

        if t == 0:
            return sum(values)
        elif t == 1:
            p = 1
            for x in values:
                p *= x
            return p
        elif t == 2:
            return min(values)
        elif t == 3:
            return max(values)
        elif t == 5:
            return int(values[0] > values[1])
        elif t == 6:
            return int(values[0] < values[1])
        elif t == 7:
            return int(values[0] == values[1])


print('ans v2:', decode(stream[::]))
print(all_versions)
print('ans v1:', sum(all_versions))
