# https://adventofcode.com/2022/day/25

with open('in.in', 'r') as f:
    lines = [list(l.strip()) for l in f.readlines()]

m = {
    '0': 0,
    '1': 1,
    '2': 2,
    '-': -1,
    '=': -2,
}


def convert(s):
    p = 1
    res = 0
    for c in s[::-1]:
        res = res + m[c] * p
        p *= 5

    return res


def convert_back(num):
    res = ''
    while num != 0:
        rem = num % 5

        for k, v in m.items():
            if (v + 5) % 5 == rem:
                res = k + res
                num = (num - v) // 5

    return res


nums = [convert(l) for l in lines]
sm = sum(nums)
print(f'sum: {sm}')

ans = convert_back(sm)
print(f'part1: {ans}, validation: {convert(ans)} should be equal to {sm}')
