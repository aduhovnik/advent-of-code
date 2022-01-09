# https://adventofcode.com/2021/day/19

from itertools import permutations

scanners = []
with open('in.in', 'r') as f:
    s = []
    for l in f.readlines():
        l = l.strip('\n')
        if not l:
            continue
        elif l.startswith('--'):
            if s:
                scanners.append(s)
                s = []
        else:
            s.append(list(map(int, l.split(','))))
scanners.append(s)


def combinations(xyz):
    combs = []
    for p in permutations(xyz):
        for dx in [1, -1]:
            for dy in [1, -1]:
                for dz in [1, -1]:
                    x, y, z = p
                    combs.append((x * dx, y * dy, z * dz))
    return combs


def absolute_values(vec, scans):
    new_scans = [
        (v[0] - vec[0],
         v[1] - vec[1],
         v[2] - vec[2],)
        for v in scans
    ]
    return new_scans


def restore_values(vec, scans):
    new_scans = [
        (v[0] + vec[0],
         v[1] + vec[1],
         v[2] + vec[2],)
        for v in scans
    ]
    return new_scans


MAX_M = 0


# N * N * 48 * N

def find_commons(s1, s2):
    global MAX_M
    s2_all = [combinations(v) for v in s2]
    for p1 in s1:
        s1_a = absolute_values(p1, s1)
        for i in range(len(s2_all[0])):
            s2_pos = [v[i] for v in s2_all]
            for p2 in s2_pos:
                s2_a = {v for v in absolute_values(p2, s2_pos)}
                common = []
                for v in s1_a:
                    if v in s2_a:
                        common.append(v)

                if len(common) >= 12:
                    print('merging!')
                    print(len(common))
                    dist = abs(-p2[0] + p1[0]) + abs(-p2[1] + p1[1]) + abs(-p2[2] + p1[2])
                    MAX_M = max(MAX_M, dist)
                    return restore_values(p1, s2_a), (-p2[0] + p1[0], -p2[1] + p1[1], -p2[2] + p1[2])


_coords = [None for i in range(len(scanners))]
removed = set()
while len(removed) + 1 != len(scanners):
    i = 0
    for j in range(i + 1, len(scanners)):
        if j in removed:
            continue
        ret = find_commons(scanners[i], scanners[j])
        if not ret:
            continue
        else:
            new, coords = ret
            _coords[j] = coords
            removed.add(j)
        print('merge', i, j)
        scanners[i] = list(set(list(map(tuple, scanners[i] + new))))

    print('round')
    print(len(removed))
    print(MAX_M)
    print('------')

print('Ans part 1:', len(scanners[0]))
print(MAX_M)
print(_coords)
max_m = 0
for i in range(1, len(scanners)):
    for j in range(1, len(scanners)):
        max_m = max(max_m, abs(_coords[i][0] - _coords[j][0]) + abs(_coords[i][1] - _coords[j][1]) + abs(
            _coords[i][2] - _coords[j][2]))
print('Ans part 2:', max_m)
