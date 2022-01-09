# https://adventofcode.com/2021/day/17

# target area: x=269..292, y=-68..-44
x0 = 269
x1 = 292
y0 = -68
y1 = -44

max_y = 0
cnt = 0
for vxx in range(0, 300):
    for vyy in range(-100, 300):
        vx = vxx
        vy = vyy
        x = 0
        y = 0
        fine = False
        mx_y = 0
        while True:
            x += vx
            y += vy
            vx = max(0, vx - 1)
            vy -= 1
            mx_y = max(y, mx_y)
            if x0 <= x <= x1 and y0 <= y <= y1:
                fine = True

            if y < min(y1, y0) or x > max(x0, x1):
                break
        if fine:
            cnt += 1
            print('hit:', mx_y, vxx, vyy)
            max_y = max(max_y, mx_y)

print('Ans part 1:', max_y)
print('Ans part 2:', cnt)
