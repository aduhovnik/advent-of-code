# https://adventofcode.com/2022/day/23
from collections import defaultdict

with open('in.in', 'r') as f:
    lines = [list(l.strip()) for l in f.readlines()]

elves = []
elves_set = set()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            elves.append((y, x))
            elves_set.add((y, x))

elves_directions = ['N', 'S', 'W', 'E']

direction_mapping = {
    'N': ((-1, -1), (-1, 0), (-1, 1)),
    'S': ((1, -1), (1, 0), (1, 1)),
    'W': ((1, -1), (0, -1), (-1, -1)),
    'E': ((1, 1), (0, 1), (-1, 1)),
}

for r in range(10000):
    suggested_cells = [None for _ in elves]
    suggested_directions = [None for _ in elves]
    for idx, (y, x) in enumerate(elves):
        number_of_neighbours = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0: continue
                ny = dy + y
                nx = dx + x
                if (ny, nx) in elves_set:
                    number_of_neighbours += 1

        if number_of_neighbours == 0:
            continue

        for d in elves_directions:
            can_go = True
            for (dy, dx) in direction_mapping[d]:
                ny = y + dy
                nx = x + dx
                can_go &= (ny, nx) not in elves_set

            if can_go:
                suggested_cells[idx] = (y + direction_mapping[d][1][0], x + direction_mapping[d][1][1])
                suggested_directions[idx] = d
                break

    cells_count = defaultdict(int)
    number_of_moves = 0
    for c in suggested_cells:
        if c:
            cells_count[c] += 1
            number_of_moves += 1

    if number_of_moves == 0:
        print('Part2: ', r + 1)
        break

    for idx in range(len(elves)):
        c = suggested_cells[idx]
        if cells_count[c] == 1:
            elves[idx] = c

    elves_set = set()
    for e in elves:
        elves_set.add(e)

    elves_directions = elves_directions[1:] + elves_directions[:1]

    if r % 50 == 0:
        print(f'round {r}')

    if r + 1 == 10:
        xs = [v[1] for v in elves]
        ys = [v[0] for v in elves]

        print(min(xs), max(xs))
        print(min(ys), max(ys))

        part1_ans = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) - len(elves)
        print(f'part1: {part1_ans}')
