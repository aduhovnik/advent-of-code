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


def common_part(a, b):
    if a[0] <= b[1] <= a[1] or b[0] <= a[1] <= b[1]:
        return max(a[0], b[0]), min(a[1], b[1])
    else:
        return None

cubes = dict()
for c0, xx0, yy0, zz0 in commands:
    _cubes = cubes.copy()

    key = (c0, xx0, yy0, zz0)

    for (c1, xx1, yy1, zz1), cnt in cubes.items():
        xc = common_part(xx0, xx1)
        yc = common_part(yy0, yy1)
        zc = common_part(zz0, zz1)

        if xc and yc and zc:
            if c1 == 'on':
                inter_key = ('off', xc, yc, zc)
                _cubes[inter_key] = _cubes.get(inter_key, 0) + cnt
            else:
                inter_key = ('on', xc, yc, zc)
                _cubes[inter_key] = _cubes.get(inter_key, 0) + cnt

    cubes = _cubes
    if c0 == 'on':
        cubes[key] = cubes.get(key, 0) + 1


def dist(a):
    return a[1] - a[0] + 1


print(len(cubes))
ans = 0
for (c0, xx0, yy0, zz0), cnt in cubes.items():
    ans += dist(xx0) * dist(yy0) * dist(zz0) * cnt * (1 if c0 == 'on' else -1)

print('Ans part 2: ', ans)
assert ans == 1160011199157381
end = time.time()
print('Time: ', end - start)
