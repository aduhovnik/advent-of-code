# https://adventofcode.com/2021/day/13

m = []
instructions = []
with open('in.in', 'r') as f:
    do_instructions = False
    for l in f.readlines():
        l = l.strip('\n')
        if not l:
            do_instructions = True
            continue

        if do_instructions:
            c, val = l.split(' ')[2].split('=')
            instructions.append((c, int(val)))
        else:
            x, y = map(int, l.strip('\n').split(','))
            m.append((x, y))

print(m)
print(instructions)

mx = max(v[0] for v in m)
my = max(v[1] for v in m)
print(mx, my)

grid = [[0 for i in range(mx + 1)] for j in range(my + 1)]
for x, y in m:
    grid[y][x] = 1


def rotate90(g):
    n_g = []
    for x in range(len(g[0])):
        new_l = []
        for y in range(len(g)):
            new_l.append(g[y][x])
        n_g.append(new_l)
    return n_g


for idx, (c, val) in enumerate(instructions):
    if c == 'x':
        # make it Y
        grid = rotate90(grid)

    # fold by Y coordinate
    for y in range(val + 1, len(grid)):
        delta = y - val
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                grid[val - delta][x] = 1

    grid = grid[:val]

    if c == 'x':
        grid = rotate90(grid)
        grid = rotate90(grid)
        grid = rotate90(grid)

    print('Ans: ', sum(v for u in grid for v in u))
    print()

for l in grid:
    print(''.join(map(lambda x: '#' if x == 1 else ' ', l)))
