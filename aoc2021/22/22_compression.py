# https://adventofcode.com/2021/day/21

import time

start = time.time()

commands = []
with open('in.in', 'r') as f:
    for l in f.readlines():
        l = l.strip('\n')
        cmd, r = l.split(' ')
        x, y, z = map(lambda x: x[2:].split('..'), r.split(','))
        commands.append((cmd, (int(x[0]), int(x[1])), (int(y[0]), int(y[1])), (int(z[0]), int(z[1]))))

x, y, z = set(), set(), set()
compression = [
    dict(),
    dict(),
    dict(),
]
for c, xx, yy, zz in commands:
    x.add(xx[0])
    x.add(xx[1] + 1)
    y.add(yy[0])
    y.add(yy[1] + 1)
    z.add(zz[0])
    z.add(zz[1] + 1)

x = list(sorted(list(x)))
x = [x[0] - 1] + x

y = list(sorted(list(y)))
y = [y[0] - 1] + y

z = list(sorted(list(z)))
z = [z[0] - 1] + z

for idx, xx in enumerate(x):
    compression[0][xx] = idx
for idx, yy in enumerate(y):
    compression[1][yy] = idx
for idx, zz in enumerate(z):
    compression[2][zz] = idx

max_x = len(x) + 1
max_y = len(y) + 1
max_z = len(z) + 1

print('creating cube...')
cube = [[[False for zz in range(max_z)] for yy in range(max_y)] for xx in range(max_x)]

print('init done')
for idx, (c0, xx0, yy0, zz0) in enumerate(commands):
    print(f'command {idx} out of {len(commands)}..')
    x0 = compression[0][xx0[0]]
    x1 = compression[0][xx0[1] + 1]
    y0 = compression[1][yy0[0]]
    y1 = compression[1][yy0[1] + 1]
    z0 = compression[2][zz0[0]]
    z1 = compression[2][zz0[1] + 1]
    for xx in range(x0, x1):
        for yy in range(y0, y1):
            for zz in range(z0, z1):
                cube[xx][yy][zz] = True if c0 == 'on' else False

print('calculating answer..')
ans = 0
for xx in range(max_x):
    for yy in range(max_y):
        for zz in range(max_z):
            if cube[xx][yy][zz]:
                x_sz = x[xx + 1] - x[xx]
                y_sz = y[yy + 1] - y[yy]
                z_sz = z[zz + 1] - z[zz]
                add = x_sz * y_sz * z_sz
                ans += add

print('Ans part 2:', ans)
assert ans == 1160011199157381
