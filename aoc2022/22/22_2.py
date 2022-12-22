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

print(y, x)

#       r  d  l  u
dirs = [0, 1, 2, 3]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

known_transitions = {}
change_dir = {}

# 0 up
for i in range(50):
    known_transitions[-1, 50 + i] = (150 + i, 0)
    change_dir[-1, 50 + i] = 0

# 0 left
    known_transitions[i, 49] = (150 - 1 - i, 0)
    change_dir[i, 49] = 0

# 1 up
    known_transitions[-1, 100 + i] = (200 - 1, i)
    change_dir[-1, 100 + i] = 3

# 1 right
    known_transitions[i, 150] = (150 - 1 - i, 99)
    change_dir[i, 150] = 2

# 1 down
    known_transitions[50, 100 + i] = (50 + i, 99)
    change_dir[50, 100 + i] = 2

# 2 left
    known_transitions[50 + i, 49] = (100, i)
    change_dir[50 + i, 49] = 1

# 2 right
    known_transitions[50 + i, 100] = (49, 100 + i)
    change_dir[50 + i, 100] = 3

# 3 up
    known_transitions[99, i] = (50 + i, 50)
    change_dir[99, i] = 0

# 3 left
    known_transitions[100 + i, -1] = (49 - i, 50)
    change_dir[100 + i, -1] = 0

# 4 right
    known_transitions[100 + i, 100] = (49 - i, 150 - 1)
    change_dir[100 + i, 100] = 2

# 4 down
    known_transitions[150, 50 + i] = [150 + i, 49]
    change_dir[150, 50 + i] = 2

# 5 left
    known_transitions[150 + i, -1] = (0, 50 + i)
    change_dir[150 + i, -1] = 1

# 5 right
    known_transitions[150 + i, 50] = (150 - 1, 50 + i)
    change_dir[150 + i, 50] = 3

# for 5 down
    known_transitions[200, i] = (0, 100 + i)
    change_dir[200, i] = 1

direction = 0
for m in moves:
    if m == 'L':
        direction = (direction - 1 + 4) % 4
        continue

    if m == 'R':
        direction = (direction + 1) % 4
        continue

    for v in range(m):
        nx = x + dx[direction]
        ny = y + dy[direction]
        new_direction = direction
        if (ny, nx) in known_transitions:
            new_direction = change_dir[ny, nx]
            ny, nx = known_transitions[ny, nx]

        if 0 <= nx < M and 0 <= ny < N and grid[ny][nx] == '#':
            break

        assert(grid[ny][nx] != ' ')

        x, y = nx, ny
        direction = new_direction

print(x, y, direction, 1000 * (y + 1) + 4 * (x + 1) + direction)
