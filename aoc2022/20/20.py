# https://adventofcode.com/2022/day/20
from copy import deepcopy

numbers = []
with open('in.in', 'r') as f:
    for i, l in enumerate(f.readlines()):
        val = int(l.strip())
        numbers.append((val, i))


def solve(nums, iterations):
    origin = deepcopy(nums)
    n = len(origin)
    for _ in range(iterations):
        for it, (v, i) in enumerate(origin):
            idx = nums.index((v, i))
            nums.pop(idx)
            new_idx = (idx + v) % len(nums)
            nums.insert(new_idx, (v, i))

    (zero_idx, _), = filter(lambda x: x[1][0] == 0, enumerate(nums))

    a = nums[(zero_idx + 1000) % n][0]
    b = nums[(zero_idx + 2000) % n][0]
    c = nums[(zero_idx + 3000) % n][0]
    print(a, b, c, a + b + c)

    return a + b + c


print(f'part1: {solve(deepcopy(numbers), 1)}')

key = 811589153

numbers = [(v[0] * key, v[1]) for v in numbers]
print(f'part2: {solve(deepcopy(numbers), 10)}')
