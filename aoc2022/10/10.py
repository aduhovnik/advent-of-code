# https://adventofcode.com/2022/day/10

with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

vals = []

idx = 0
val = 1


sprite = [['.' for i in range(40)] for j in range(6)]


def update_sprite():
    y = idx // 40
    x = idx % 40
    if x in (val - 1, val, val + 1):
        sprite[y][x] = '#'


def check():
    if idx in (20, 60, 100, 140, 180, 220):
        vals.append(val * idx)


for i in ls:
    if i == 'noop':
        update_sprite()
        idx += 1
        check()
    else:
        _, inc = i.split()
        inc = int(inc)
        update_sprite()
        idx += 1
        check()
        update_sprite()
        idx += 1
        check()
        val += inc

print('part1')
print(sum(vals))

print()
print('part2')
for v in sprite:
    print(''.join(v))

