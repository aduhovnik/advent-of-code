# https://adventofcode.com/2021/day/15

from queue import Queue

grid0 = []
with open('in.in', 'r') as f:
    for l in f.readlines():
        l = l.strip('\n')
        grid0.append(list(map(int, l)))

inf = 1e18
n = len(grid0)
m = len(grid0[0])
grid = [[0 for i in range(m * 5)] for j in range(n * 5)]
for ii in range(5):
    for jj in range(5):
        for i in range(n):
            for j in range(m):
                nx = ii * n + i
                ny = jj * m + j
                grid[nx][ny] = (grid0[i][j] + ii + jj - 1) % 9 + 1

n = len(grid)
m = len(grid[0])
dp = [[inf for i in range(m)] for j in range(n)]
dp[0][0] = 0
q = Queue()
q.put((0, 0))
s = set()
s.add((0, 0))

DX = [0, 0, 1, -1]
DY = [-1, 1, 0, 0]
while not q.empty():
    (x, y) = q.get()
    s.remove((x, y))
    for idx in range(4):
        nx = x + DX[idx]
        ny = y + DY[idx]
        if 0 <= nx < n and 0 <= ny < m:
            if dp[nx][ny] > dp[x][y] + grid[nx][ny]:
                dp[nx][ny] = dp[x][y] + grid[nx][ny]
                if (nx, ny) not in s:
                    q.put((nx, ny))
                    s.add((nx, ny))

print(dp[n-1][m-1])
