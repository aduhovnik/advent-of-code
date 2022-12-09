# https://adventofcode.com/2022/day/9

ls = []
with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]


def solve(length):
    visited = set()
    rope = [(0, 0) for _ in range(length)]

    for l in ls:
        w, n = l.split()
        n = int(n)
        if w == 'R':
            dx, dy = 1, 0
        elif w == 'L':
            dx, dy = -1, 0
        elif w == 'U':
            dx, dy = 0, 1
        else:
            dx, dy = 0, -1

        for i in range(n):
            _new_rope = []

            new_cur = rope[0]
            new_cur = (new_cur[0] + dx, new_cur[1] + dy)
            _new_rope.append(new_cur)

            def sign(val):
                return 1 if val > 0 else -1

            for j in range(1, length):
                cur_h = new_cur
                cur_t = rope[j]
                delta_x = abs(cur_h[0] - cur_t[0])
                delta_y = abs(cur_h[1] - cur_t[1])
                fine = max(delta_y, delta_x) <= 1
                if not fine:
                    ddx = cur_h[0] - cur_t[0]
                    ddy = cur_h[1] - cur_t[1]
                    if abs(ddx) + abs(ddy) > 2:
                        cur_t = (cur_t[0] + sign(ddx), cur_t[1] + sign(ddy))
                    elif abs(ddx) == 2:
                        cur_t = (cur_t[0] + sign(ddx), cur_t[1])
                    elif abs(ddy) == 2:
                        cur_t = (cur_t[0], cur_t[1] + sign(ddy))

                delta_x = abs(cur_h[0] - cur_t[0])
                delta_y = abs(cur_h[1] - cur_t[1])
                assert max(delta_y, delta_x) <= 1

                _new_rope.append(cur_t)
                new_cur = cur_t

            assert len(_new_rope) == length
            visited.add(_new_rope[-1])
            rope = _new_rope

    return len(visited)


print(solve(2))
print(solve(10))
