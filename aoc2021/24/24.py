p1 = []
p2 = []
p3 = []
cnt = 0
with open('in.in', 'r') as f:
    for l in f.readlines():
        l = l.strip('\n')
        if l.startswith('inp'):
            cnt = 0
        if cnt == 4:
            p = int(l.split(' ')[2])
            p1.append(p)
        elif cnt == 5:
            p = int(l.split(' ')[2])
            p2.append(p)
        elif cnt == 15:
            p = int(l.split(' ')[2])
            p3.append(p)

        cnt += 1

print(', '.join(list(map(lambda x: str(x).rjust(3, ' '), range(14)))))
print(', '.join(list(map(lambda x: str(x).rjust(3, ' '), p1))))
print(', '.join(list(map(lambda x: str(x).rjust(3, ' '), p2))))
print(', '.join(list(map(lambda x: str(x).rjust(3, ' '), p3))))

z = 0


def round(input_w, p1, p2, p3):
    global z
    x = 0
    x *= 0  # 0
    x += z  # accumulate
    x %= 26
    z /= p1  # (p1 == 1 for 7 first times and 26 for last 7 times)
    x += p2
    x = int(x != input_w)  # 0 if eq 1 if not
    y = 0
    y *= 0  # 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += input_w
    y += p3
    y *= x
    z += y


def round1(w, p1, p2, p3):
    global z
    x = int(z % 26 + p2 != w)  # 1 or 0
    z //= p1  # loose one last digit
    y = 25 * x + 1  # (26 or 1)
    z *= y  # either add 26 degree or not
    y = (w + p3) * x
    z += y  # add new last digit


def validate(nums: int):
    nums = [int(v) for v in str(nums)]
    global z
    z = 0
    for i in range(14):
        round1(nums[i], p1[i], p2[i], p3[i])
    assert z == 0


def solve(mode='max'):
    stack = []
    pairs = []  # id1, id2, what to add to id1
    for i in range(14):
        # where p1 == 1 we can only add one digits
        # where p1 == 26 we can remove one last digit
        if p1[i] == 1:  # adding digit
            stack.append((i, p3[i]))
        else:
            id1, p3_idx1 = stack.pop(-1)
            id2 = i
            pairs.append((id1, id2, p3_idx1 + p2[i]))

    answer = [0 if mode == 'max' else 100 for _ in range(14)]
    for id1, id2, addition in pairs:
        for v in range(1, 10):
            for u in range(1, 10):
                if v + addition != u:
                    continue
                if mode == 'min':
                    answer[id1] = min(answer[id1], v)
                    answer[id2] = min(answer[id2], u)
                else:
                    answer[id1] = max(answer[id1], v)
                    answer[id2] = max(answer[id2], u)
    return int(''.join(map(str, answer)))


part1 = solve('max')
validate(part1)
print(f'Part 1: {part1}')
part2 = solve('min')
validate(part2)
print(f'Part 2: {part2}')
