# https://adventofcode.com/2022/day/24

with open('in.in', 'r') as f:
    lines = [list(l.strip()) for l in f.readlines()]

grid = [list(l) for l in lines]

directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}

MAX_DAYS = 1000
n, m = len(grid), len(grid[0])

blizzards = []
for y, l in enumerate(grid):
    for x, c in enumerate(l):
        if c in '<>^v':
            blizzards.append((y, x, c))


def generate_next_blizzards(cur_blizzards):
    _blizzards = []
    for y, x, direction in cur_blizzards:
        dy, dx = directions[direction]
        ny, nx = y + dy, x + dx
        if grid[ny][nx] == '#':
            ny, nx = ny + -1 * dy * (n - 2), nx + -1 * dx * (m - 2)

        _blizzards.append((ny, nx, direction))

    return _blizzards


blizzard_positions = {
    0: blizzards
}

for day in range(1, MAX_DAYS):
    blizzards = generate_next_blizzards(blizzards)
    blizzard_positions[day] = blizzards

dist = [[[-1 for i in range(m)] for j in range(n)] for k in range(MAX_DAYS)]
dist[0][0][1] = 0

DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

ans_part1 = float('inf')
ans_part2 = float('inf')

for day in range(MAX_DAYS - 1):
    if ans_part2 < float('inf'):
        break

    cur_blizzards = blizzard_positions[day]
    next_blizzards = blizzard_positions[day + 1]
    cur_blizzards_set = set([(b[0], b[1]) for b in cur_blizzards])
    next_blizzards_set = set([(b[0], b[1]) for b in next_blizzards])

    for y in range(n):
        for x in range(m):

            if dist[day][y][x] == -1 or (y, x) in cur_blizzards_set:
                continue

            value = dist[day][y][x]

            if (y, x) == (n - 1, m - 2) and value == 0:
                ans_part1 = day
                value = 1

            if (y, x) == (0, 1) and value == 1:
                value = 2

            if (y, x) == (n - 1, m - 2) and value == 2:
                ans_part2 = day

            for i in range(4):
                dx, dy = DX[i], DY[i]
                ny, nx = y + dy, x + dx

                if (ny, nx) in next_blizzards_set:
                    continue

                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue

                if grid[ny][nx] == '#':
                    continue

                dist[day + 1][ny][nx] = max(dist[day + 1][ny][nx], value)

            dist[day + 1][y][x] = max(dist[day + 1][y][x], value)


print(f'part1: {ans_part1}')
print(f'part2: {ans_part2}')
