# https://adventofcode.com/2022/day/22

with open('in.in', 'r') as f:
    lines = [l.strip('\n') for l in f.readlines()]

grid = []
moves = None

is_moves = False
for l in lines:
    if not l:
        is_moves = True
        continue

    if is_moves:
        moves = l
    else:
        grid.append(l)


parsed_moves = []
cur = ''
for c in moves:
    if c in 'LR':
        parsed_moves.append(int(cur))
        parsed_moves.append(c)
        cur = ''
    else:
        cur += c

parsed_moves.append(int(cur))
moves = parsed_moves

N = len(grid)
M = max(len(v) for v in grid)
grid = [list(v.ljust(M, ' ')) for v in grid]

x, y = 0, 0
for i in range(len(grid[0])):
    if grid[0][i] == '.':
        x = i
        break

print(x, y)

dirs = [0, 1, 2, 3]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


direction = 0
for m in moves:
    if m == 'L':
        direction = (direction - 1 + 4) % 4
        continue

    if m == 'R':
        direction = (direction + 1) % 4
        continue

    for v in range(m):
        nx = (x + dx[direction] + M) % M
        ny = (y + dy[direction] + N) % N

        while grid[ny][nx] == ' ':
            nx = (nx + dx[direction] + M) % M
            ny = (ny + dy[direction] + N) % N
            if grid[ny][nx] == '#':
                break

        if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == '#':
            break

        x, y = nx, ny


print(x, y, direction, 1000 * (y + 1) + 4 * (x + 1) + direction)
