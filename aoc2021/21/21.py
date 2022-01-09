# https://adventofcode.com/2021/day/21

from functools import lru_cache

p1 = 4
p2 = 8
s1 = 0
s2 = 0

all_moves = []
for i in range(1, 4):
    for k in range(1, 4):
        for j in range(1, 4):
            all_moves.append(i + k + j)
all_moves.sort()
print(all_moves)


def merge(a, b):
    return a[0] + b[0], a[1] + b[1]


@lru_cache(maxsize=10 ** 10)
def rec(pos1, pos2, p1=0, p2=0, t=0):
    if p1 >= 21:
        return 1, 0
    elif p2 >= 21:
        return 0, 1
    res = (0, 0)
    if t % 2 == 0:
        # p1
        for m in all_moves:
            new_pos1 = (pos1 - 1 + m) % 10 + 1
            sub_res = rec(new_pos1, pos2, p1 + new_pos1, p2, t + 1)
            res = merge(res, sub_res)
    else:
        # p2
        for m in all_moves:
            new_pos2 = (pos2 - 1 + m) % 10 + 1
            sub_res = rec(pos1, new_pos2, p1, p2 + new_pos2, t + 1)
            res = merge(res, sub_res)

    return res


ans = rec(p1, p2)
print(max(ans))
