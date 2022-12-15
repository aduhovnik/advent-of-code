# https://adventofcode.com/2022/day/15
import re

with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]


sensors, beacons = [], []
for l in ls:
    xs, ys, xb, yb = map(int, re.findall('=(-?[0-9]+)', l))
    sensors.append((xs, ys))
    beacons.append((xb, yb))


MX = 4000000

for row in range(0, MX):
    used_in_row = []

    for i in range(len(sensors)):
        s_x, s_y = sensors[i]
        b_x, b_y = beacons[i]

        dist = abs(s_x - b_x) + abs(s_y - b_y)
        dist_to_row_y = abs(s_y - row)
        if dist_to_row_y > dist:
            continue

        dx = dist - dist_to_row_y
        used_in_row.append((s_x - dx, s_x + dx))

    used_in_row.sort()
    prev_end = 0
    for s, e in used_in_row:
        if s <= prev_end + 1:
            prev_end = max(e, prev_end)
        else:
            print(f'part 2 answer: {row + (prev_end + 1) * MX}')
            exit(0)
