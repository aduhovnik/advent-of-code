# https://adventofcode.com/2022/day/13
from functools import cmp_to_key

with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

pairs = []
pair = []
for l in ls:
    if l:
        pair.append(eval(l))
    else:
        pairs.append(pair)
        pair = []

pairs.append(pair)

correct = []


def compare(l, r):
    if type(l) == int and type(r) == int:
        if l == r: return 0
        if l < r: return -1
        return 1

    if type(l) == list and type(r) == int:
        return compare(l, [r])

    if type(l) == int and type(r) == list:
        return compare([l], r)

    if type(l) == list and type(r) == list:
        for i in range(min(len(l), len(r))):
            res = compare(l[i], r[i])
            if res != 0:
                return res

        return compare(len(l), len(r))


for idx, pair in enumerate(pairs):
    if compare(*pair) < 0:
        correct.append(idx + 1)

print('part1:')
print(sum(correct))

all_pockets = [[[2]], [[6]]]
for p in pairs:
    all_pockets.extend(p)

all_pockets = sorted(all_pockets, key=cmp_to_key(compare))

ans = []
for idx, p in enumerate(all_pockets):
    if p in [[[2]], [[6]]]:
        ans.append(idx + 1)

print('part2:')
print(ans[1] * ans[0])
