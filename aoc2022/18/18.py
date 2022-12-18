# https://adventofcode.com/2022/day/18
from queue import Queue

with open('in.in', 'r') as f:
    lava = [list(map(int, l.strip().split(','))) for l in f.readlines()]

m = [[[False for _ in range(64)] for __ in range(64)] for ___ in range(64)]

for x, y, z in lava:
    m[x][y][z] = True

deltas = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0)
]

ans = 0
for x in range(64):
    for y in range(64):
        for z in range(64):
            if not m[x][y][z]:
                continue

            for dx, dy, dz in deltas:
                nx, ny, nz = x + dx, y + dy, z + dz
                if not m[nx][ny][nz]:
                    ans += 1

print(ans)

used = [[[False for _ in range(64)] for __ in range(64)] for ___ in range(64)]
reachable = [[[False for _ in range(64)] for __ in range(64)] for ___ in range(64)]

q = Queue()

q.put((0, 0, 0))
while not q.empty():
    x, y, z = q.get()
    used[x][y][z] = True
    for dx, dy, dz in deltas:
        nx, ny, nz = x + dx, y + dy, z + dz

        reachable[nx][ny][nz] = True
        if m[nx][ny][nz]:
            continue

        if used[nx][ny][nz]:
            continue

        used[nx][ny][nz] = True
        q.put((nx, ny, nz))

ans = 0
for x in range(64):
    for y in range(64):
        for z in range(64):
            if not m[x][y][z]:
                continue

            for dx, dy, dz in deltas:
                nx, ny, nz = x + dx, y + dy, z + dz
                if not m[nx][ny][nz] and reachable[nx][ny][nz]:
                    ans += 1

print(ans)
