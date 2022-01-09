from copy import deepcopy

tiles_ids = []
tiles = []

with open('in.in', 'r') as f:
    while True:
        t = f.readline().strip('\n:')
        if t == '':
            break

        _, num = t.split(' ')
        tiles_ids.append(int(num))
        tile = []
        for i in range(10):
            tile.append(f.readline().strip('\n'))
        tiles.append(tile.copy())

        f.readline()

n = int(len(tiles) ** 0.5)
N = 10


def rotate90(m):
    new_m = []
    for i in range(len(m)):
        new_row = []
        for j in range(len(m[0])):
            new_row.append(m[len(m) - j - 1][i])
        new_m.append(''.join(new_row))
    return new_m


def flip_h(m):
    return [v[::-1] for v in m]


def flip_v(m):
    new_m = []
    for i in range(len(m)):
        new_row = []
        for j in range(len(m[0])):
            new_row.append(m[len(m) - i - 1][j])
        new_m.append(''.join(new_row))
    return new_m


def get_left(m):
    return ''.join([m[i][0] for i in range(N)])


def get_right(m):
    return ''.join([m[i][-1] for i in range(N)])


def get_top(m):
    return m[0]


def get_bot(m):
    return m[-1]


print('\n'.join(tiles[0]))
print()
print('\n'.join(rotate90(tiles[0])))
print()
print('\n'.join(flip_h(tiles[0])))
print()
print('\n'.join(flip_v(tiles[0])))
print('validated rotation')


def check_grid(g, i, j) -> bool:
    if g[i][j] is None:
        return False

    if i > 0:
        if g[i - 1][j] is not None and get_bot(g[i - 1][j]) != get_top(g[i][j]):
            return False
    if i < n - 1:
        if g[i + 1][j] is not None and get_bot(g[i][j]) != get_top(g[i + 1][j]):
            return False
    if j > 0:
        if g[i][j - 1] is not None and get_left(g[i][j]) != get_right(g[i][j - 1]):
            return False
    if j < n - 1:
        if g[i][j + 1] is not None and get_left(g[i][j + 1]) != get_left(g[i][j]):
            return False

    return True


grid = [[None for i in range(n)] for j in range(n)]
grid_ids = [[None for i in range(n)] for j in range(n)]
grid_idxs = [[None for i in range(n)] for j in range(n)]
solved = False
solution_grid = [[None for i in range(n)] for j in range(n)]
solution_grid_ids = [[None for i in range(n)] for j in range(n)]
used_tiles = [False for i in range(len(tiles))]
print(check_grid(grid, 0, 0))


def get_all_positions(m):
    not_rotated_tiles = [m, flip_h(m), flip_v(m), flip_h(flip_v(m))]
    all_possible_tiles = []
    for t in not_rotated_tiles:
        for r in range(4):
            t = rotate90(t)
            all_possible_tiles.append(t)
    return all_possible_tiles


# pre-calc
all_pos = [get_all_positions(t) for t in tiles]
possible_neighbours = []
for i in range(len(tiles)):
    print(f'finding neighbours: {i}')
    possible_neighbours.append(set())
    for j in range(len(tiles)):
        if j == i:
            continue

        g = [[None, None, None], [None, None, None]]
        for t1 in all_pos[i]:
            for t2 in all_pos[j]:
                g[0][0] = t1
                g[0][1] = t2
                if check_grid(g, 0, 1):
                    possible_neighbours[-1].add(j)


def solve(depth=0):
    global solved

    if solved:
        return

    print(f'depth: {depth}, used: {sum(used_tiles)}')
    if sum(used_tiles) == n * n:
        global solution_grid
        global solution_grid_ids
        solved = True
        solution_grid = deepcopy(grid)
        solution_grid_ids = deepcopy(grid_ids)
        return

    tried_to_insert = False
    for i in range(n):
        if tried_to_insert:
            break
        for j in range(n):
            if tried_to_insert:
                break

            if grid[i][j] is None:
                if i == 0 and j == 0:
                    possible_n = [i for i in range(len(tiles)) if len(possible_neighbours[i]) == 2]  # range(len(tiles))
                elif j == 0:
                    possible_n = possible_neighbours[grid_idxs[i-1][0]]
                else:
                    possible_n = possible_neighbours[grid_idxs[i][j-1]]

                for idx in possible_n:
                    tried_to_insert = True

                    if used_tiles[idx]:
                        continue

                    # applying
                    used_tiles[idx] = True
                    cur_tile_id = tiles_ids[idx]
                    grid_ids[i][j] = cur_tile_id
                    grid_idxs[i][j] = idx

                    for t in all_pos[idx]:
                        grid[i][j] = t
                        if check_grid(grid, i, j):
                            print(f'tile id: {cur_tile_id}')
                            solve(depth=depth + 1)

                    # cleaning
                    used_tiles[idx] = False
                    grid[i][j] = None
                    grid_ids[i][j] = None
                    grid_idxs[i][j] = None


solve()
print(solved)
print(solution_grid_ids)
print('ANSWER Part 1:')
print(solution_grid_ids[0][0] * solution_grid_ids[0][-1] * solution_grid_ids[-1][0] * solution_grid_ids[-1][-1])


mask = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]

full_grid = [[' ' for i in range(8 * n)] for j in range(8 * n)]
for x, v in enumerate(solution_grid):
    for y, m in enumerate(v):
        for xx in range(1, 9):
            for yy in range(1, 9):
                real_x = x * 8 + xx - 1
                real_y = y * 8 + yy - 1
                full_grid[real_x][real_y] = m[xx][yy]

NN = n * 8

print('New grid:')
for row in full_grid:
    print(''.join(row))


def rotate900(m):
    new_m = []
    for i in range(len(m)):
        new_row = []
        for j in range(len(m[0])):
            new_row.append(m[len(m) - j - 1][i])
        new_m.append(new_row)
    return new_m


def flip_hh(m):
    return [v[::-1] for v in m]


def flip_vv(m):
    new_m = []
    for i in range(len(m)):
        new_row = []
        for j in range(len(m[0])):
            new_row.append(m[len(m) - i - 1][j])
        new_m.append(new_row)
    return new_m


all_grids = [flip_vv(full_grid), flip_hh(full_grid), flip_hh(flip_vv(full_grid)), full_grid]
min_cnt = 100**100

for g in all_grids:
    for _ in range(4):
        g = rotate900(g)

        for i in range(NN - len(mask)):
            for j in range(NN - len(mask[0])):
                match = True
                for ii in range(len(mask)):
                    for jj in range(len(mask[0])):
                        if mask[ii][jj] == '.':
                            if mask[ii][jj] == g[i + ii][j + jj]:
                                match &= True
                            else:
                                match &= False

                if match:
                    for ii in range(len(mask)):
                        for jj in range(len(mask[0])):
                            if mask[ii][jj] == '.':
                                g[i + ii][j + jj] = ' '

        cnt = sum(v == '.' for u in g for v in u)
        min_cnt = min(min_cnt, cnt)

print('ANSWER Part 2:', min_cnt)
