# https://adventofcode.com/2022/day/11
from copy import deepcopy
from queue import Queue

with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

monkeys = []

monkey = []
for l in ls:
    l = l.strip()

    if l.startswith('Monkey') and monkey:
        monkeys.append(monkey)
        monkey = []
        continue

    if l.startswith('Starting items'):
        _, items = l.split(':')
        items = list(map(int, items.split(', ')))
        monkey.append(items)
        continue

    if l.startswith('Operation'):
        _, op = l.split(':')
        monkey.append(op)
        continue

    if l.startswith('Test'):
        div = int(l.split()[-1])
        monkey.append(div)
        continue

    if l.startswith('If true'):
        num = int(l.split()[-1])
        monkey.append(num)
        continue

    if l.startswith('If false'):
        num = int(l.split()[-1])
        monkey.append(num)
        continue

monkeys.append(monkey)

all_divs = [m[2] for m in monkeys]
ml = 1
for d in all_divs:
    ml *= d


def do_op(op, cur_value):
    op = op.split(' = ')[1]
    op = op.replace('old', str(cur_value))
    return eval(op)


def calc_ans(_monkeys, rounds, anxiety_level_func):
    monkeys_count = [0 for _ in monkeys]

    for m in _monkeys:
        q = Queue()
        for i in m[0]:
            q.put(i)
        m[0] = q

    for r in range(rounds):
        for idx, m in enumerate(_monkeys):
            _, op, div, tr, fl = m
            while not _monkeys[idx][0].empty():
                monkeys_count[idx] += 1
                it = _monkeys[idx][0].get()
                new_it = do_op(op, it)
                new_it = anxiety_level_func(new_it)

                to_throw = tr if new_it % div == 0 else fl

                if to_throw >= idx:
                    _monkeys[to_throw][0].put(new_it)
                else:
                    _monkeys[to_throw][0].put(new_it)

    monkeys_count.sort()
    print(monkeys_count[-1] * monkeys_count[-2])


calc_ans(deepcopy(monkeys), 20, lambda x: x // 3)
calc_ans(deepcopy(monkeys), 10000, lambda x: x % ml)
