# https://adventofcode.com/2022/day/12
from queue import Queue

with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

g = []
dist = []
start = None
stop = None
for y, l in enumerate(ls):
    row = []
    for x, c in enumerate(l):
        if c == 'S':
            c = 'a'
            start = (y, x)
        if c == 'E':
            c = 'z'
            stop = (y, x)

        c = ord(c) - ord('a')
        row.append(c)

    g.append(row)
    dist.append([10000 for i in range(len(row))])

n = len(g)
m = len(g[0])


def solve(start_from_zeros=False):
    q = Queue()
    q.put(start)
    dist[start[0]][start[1]] = 0

    if start_from_zeros:
        for y in range(n):
            for x in range(m):
                if g[y][x] == 0:
                    q.put((y, x))
                    dist[y][x] = 0

    while not q.empty():
        y, x = q.get()
        DX = [0, 0, 1, -1]
        DY = [1, -1, 0, 0]
        for i in range(4):
            ny = y + DY[i]
            nx = x + DX[i]
            if ny < 0 or ny >= n: continue
            if nx < 0 or nx >= m: continue
            delta = g[ny][nx] - g[y][x]
            if delta > 1: continue
            if dist[y][x] + 1 < dist[ny][nx]:
                dist[ny][nx] = min(dist[ny][nx], dist[y][x] + 1)
                q.put((ny, nx))

    return dist[stop[0]][stop[1]]


print('part1: ', solve(False))
print('part2: ', solve(True))
