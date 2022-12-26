# https://adventofcode.com/2022/day/25


import z3

with open('in.in', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

m = {
    '0': 0,
    '1': 1,
    '2': 2,
    '-': -1,
    '=': -2,
}
back_m = {v: k for k, v in m.items()}

total_sum = sum(sum(m[c] * 5 ** i for i, c in enumerate(l[::-1])) for l in lines)
print(f'total sum: {total_sum}')
solver = z3.Solver()
MAX_LEN = 50
variables = [z3.Int(f'val_{i}') for i in range(MAX_LEN)]
for v in variables:
    solver.add(z3.And(-2 <= v, v <= 2))

solver.add(sum(v * 5 ** i for i, v in enumerate(variables)) == total_sum)
print(solver.check())
solution = solver.model()

answer = ''.join(back_m[solution[v].as_long()] for v in variables[::-1]).lstrip('0')
print(f'part1: {answer}')
