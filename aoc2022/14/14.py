# https://adventofcode.com/2022/day/14

with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

figures = [[tuple(map(int, f.split(','))) for f in l.split(' -> ')] for l in ls]

xs = []
ys = []
for fg in figures:
    for p in fg:
        xs.append(p[0])
        ys.append(p[1])

min_x = min(xs)
max_x = max(xs)
min_y = min(0, min(ys))
max_y = max(0, max(ys))

delta_x = max_x - min_x
delta_y = max_y - min_y

m = [['.' for v in range(delta_x * 4)] for u in range(delta_y * 4)]

convert_x = lambda x: x - min_x + delta_x * 2
convert_y = lambda y: y - min_y + delta_y * 2

for fg in figures:
    fg = [(convert_x(c[0]), convert_y(c[1])) for c in fg]
    for i in range(1, len(fg)):
        s, e = fg[i-1], fg[i]
        for y in range(min(s[1], e[1]), max(s[1], e[1]) + 1):
            for x in range(min(s[0], e[0]), max(s[0], e[0])+1):
                m[y][x] = '#'

sand_x, sand_y = convert_x(500), convert_y(0)


def simulate(matrix):
    number_of_sands = 0
    stop = False
    while True:
        if stop:
            break

        x = sand_x
        y = sand_y

        while True:
            if y + 1 >= len(matrix):
                stop = True
                break

            if matrix[y + 1][x] == '.':
                y += 1

                continue
            else:
                if matrix[y + 1][x - 1] == '.':
                    x -= 1
                    y += 1
                    continue
                elif matrix[y + 1][x + 1] == '.':
                    x += 1
                    y += 1
                    continue

            if matrix[y][x] == '.':
                matrix[y][x] = 'o'
                number_of_sands += 1
            else:
                stop = True
            break

    return number_of_sands


print(f'part1: {simulate(m)}')

for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == 'o':
            m[y][x] = '.'

# part 2
for i in range(len(m[0])):
    m[convert_y(max_y + 2)][i] = '#'

print(f'part2: {simulate(m)}')
