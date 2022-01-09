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


current_cubes = []
for c0, xx0, yy0, zz0 in commands:
    _current_cubes = current_cubes.copy()

    for c1, xx1, yy1, zz1 in current_cubes:
        xc = common_part(xx0, xx1)
        yc = common_part(yy0, yy1)
        zc = common_part(zz0, zz1)
        if xc and yc and zc:
            if c0 == 'off' and c1 == 'off':
                _current_cubes.append(('on', xc, yc, zc))
            elif c0 == 'off' and c1 == 'on':
                _current_cubes.append(('off', xc, yc, zc))
            elif c0 == 'on' and c1 == 'off':
                _current_cubes.append(('on', xc, yc, zc))
            else:
                _current_cubes.append(('off', xc, yc, zc))

    current_cubes = _current_cubes
    if c0 == 'on':
        current_cubes.append((c0, xx0, yy0, zz0))


def dist(a):
    return a[1] - a[0] + 1


cnt = 0
for c0, xx0, yy0, zz0 in current_cubes:
    cnt += dist(xx0) * dist(yy0) * dist(zz0) * (-1 if c0 == 'off' else 1)

print(len(current_cubes))
print('Ans part 2: ', cnt)
end = time.time()
print('Time: ', end - start)
