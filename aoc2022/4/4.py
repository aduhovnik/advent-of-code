from collections import defaultdict

with open('in.in', 'r') as f:
    l = f.readline().strip('\n')


def solve(n):
    for idx in range(n, len(l)):
        if len(set(l[idx - n: idx])) == n:
            print(idx)
            break


solve(4)
solve(14)
