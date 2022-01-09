# https://adventofcode.com/2021/day/20

from copy import deepcopy

g = []
img = []
with open('in.in', 'r') as f:
    is_g = True
    for l in f.readlines():
        l = l.strip('\n')
        if not l:
            is_g = False
            continue
        if is_g:
            g.append(l)
        else:
            img.append(l)

g = ''.join(g)
print(g)

n = len(img)
m = len(img[0])
print(n, m)
delta = 55
N = n + delta * 2
M = m + delta * 2
mg = [['.' for i in range(N)] for j in range(M)]
for i in range(n):
    for j in range(m):
        mg[i + delta][j + delta] = img[i][j]

cnt = 50
while cnt > 0:
    cnt -= 1
    mg1 = deepcopy(mg)
    for i in range(N):
        for j in range(M):
            num = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    xx = (i + x + N) % M
                    yy = (j + y + M) % M
                    if mg[xx][yy] == '.':
                        num.append('0')
                    else:
                        num.append('1')
            num = int(''.join(num), 2)
            mg1[i][j] = g[num]

    mg = mg1

    tans = sum(v == '#' for u in mg[2:-2] for v in u[2:-2])
    print(tans)

print('Ans part 2:', tans)