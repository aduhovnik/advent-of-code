# https://adventofcode.com/2022/day/21

from sympy import Symbol, solve, Add, Mul

with open('in.in', 'r') as f:
    lines = f.readlines()

root_op, = filter(lambda x: x.startswith('root'), lines)
left_op, _, right_op = root_op.strip().split(': ')[1].split(' ')
print(left_op, right_op)

g = dict()

for l in lines:
    left, equation = l.split(': ')
    right = equation.strip().split(' ')
    if len(right) == 1:
        right = int(right[0])

    g[left] = right


operations = {
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


def dfs(v):
    equation = g[v]
    if type(equation) in (int, Symbol):
        return equation
    else:
        left, op, right = equation
        return operations[op](dfs(left), dfs(right))


print(f'part1: {dfs("root")}')

g['humn'] = Symbol('x')

left = dfs(left_op)
right = dfs(right_op)

equation = Add(left, Mul(-1, right))

print(f'part2: {round(solve(equation)[0])}')
