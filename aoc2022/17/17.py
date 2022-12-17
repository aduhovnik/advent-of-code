# https://adventofcode.com/2022/day/17

with open('in.in', 'r') as f:
    moves = f.read().strip('\n ')


figures = [
    ((0, 0), (0, 1), (0, 2), (0, 3)),

    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),

    ((0, 2), (1, 2), (2, 0), (2, 1), (2, 2)),

    ((0, 0), (1, 0), (2, 0), (3, 0)),

    ((0, 0), (0, 1), (1, 0), (1, 1))
]

W = 7


def solve(n):
    N = 5000

    grid = [['.' for _ in range(W)] for _ in range(3)]

    figure_ptr = 0
    move_ptr = 0
    previous_height = 0

    deltas = []
    for step in range(N):
        if step == n:
            return previous_height

        figure = figures[figure_ptr]
        figure_ptr = (figure_ptr + 1) % len(figures)

        ht = len(set(v[0] for v in figure))

        cnt_of_empty = 0
        while cnt_of_empty < len(grid) and grid[cnt_of_empty].count('#') == 0:
            cnt_of_empty += 1

        if cnt_of_empty > 3:
            for i in range(cnt_of_empty - 3):
                grid = grid[1:]
        else:
            while all(grid[r].count('#') > 0 for r in range(3)):
                grid = [['.' for i in range(W)]] + grid

        to_add = [['.' for _ in range(W)] for j in range(ht)]
        coordinates = []
        for f in figure:
            coordinates.append((f[0], f[1] + 2))

        grid = to_add + grid

        can_move = True
        while can_move:
            move = moves[move_ptr]
            dx = -1 if move == '<' else 1
            move_ptr = (move_ptr + 1) % len(moves)
            moved_hor = True
            new_coordinates = []
            for cycle_len in coordinates:
                new_coordinates.append((cycle_len[0], cycle_len[1] + dx))
                moved_hor &= 0 <= cycle_len[1] + dx < W
                if moved_hor:
                    moved_hor &= grid[cycle_len[0]][cycle_len[1] + dx] == '.'

            if moved_hor:
                coordinates = new_coordinates

            moved_down = True
            new_coordinates = []
            for cycle_len in coordinates:
                new_coordinates.append((cycle_len[0] + 1, cycle_len[1]))
                moved_down &= 0 <= cycle_len[0] + 1 < len(grid)
                if moved_down:
                    moved_down &= grid[cycle_len[0] + 1][cycle_len[1]] == '.'

            if moved_down:
                coordinates = new_coordinates

            if not moved_down:
                can_move = False

        for cycle_len in coordinates:
            grid[cycle_len[0]][cycle_len[1]] = '#'

        current_height = len([v for v in grid if v.count('#')])
        deltas.append(current_height - previous_height)
        previous_height = current_height

    print('deltas over rounds')
    print(deltas)

    found = False
    for st in range(1, 1000):
        if found:
            break
        for cl in range(1, 2000):
            cycle = deltas[st: st + cl]
            is_cycle = True
            cur = st
            while cur + cl < len(deltas):
                is_cycle &= cycle == deltas[cur: cur + cl]
                cur += cl

            if is_cycle:
                part_without_cycle = deltas[:st]
                print("Found cycle!")
                found = True
                break

    print('part before cycle:')
    print(part_without_cycle)
    print('cycle')
    print(cycle)

    p0_len = len(part_without_cycle)
    p0_sum = sum(part_without_cycle)
    cycle_len = len(cycle)
    cycle_sum = sum(cycle)

    current_answer = p0_sum + (n - p0_len) // cycle_len * cycle_sum
    current_steps = p0_len + (n - p0_len) // cycle_len * cycle_len
    add = 0
    while current_steps < n:
        current_steps += 1
        current_answer += cycle[add]
        add += 1

    return current_answer


print(f'part1: {solve(2022)}')
print(f'part2: {solve(1000000000000)}')
