# https://adventofcode.com/2022/day/21

with open('in.in', 'r') as f:
    lines = f.readlines()


def calc_root(override_known_values=None):
    known_values = dict()
    known_values.update(override_known_values or {})

    while 'root' not in known_values:
        for l in lines:
            m, op = l.split(':')
            if m in known_values: continue
            for k, v in known_values.items():
                op = op.replace(k, str(v))
            try:
                known_values[m] = int(eval(op))
            except Exception:
                pass

    return known_values


print(f'part1: {calc_root()["root"]}')

root_op, = filter(lambda x: x.startswith('root'), lines)
left_op, _, right_op = root_op.strip().split(': ')[1].split(' ')
print(left_op, right_op)

l = 1
r = 10**15

while l + 1 < r:
    mid = (l + r) >> 1
    known_values = calc_root({'humn': mid})

    left_op_val, right_op_val = known_values[left_op], known_values[right_op]
    print(left_op_val, right_op_val, mid)
    if left_op_val == right_op_val:
        print(f'part2: {mid}')
        break

    if left_op_val < right_op_val:
        r = mid
    else:
        l = mid
