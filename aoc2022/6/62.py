from functools import reduce

with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

n = len(ls)
m = len(ls[0])

visible = [[1 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        val = int(ls[i][j])
        ml = [0, 0, 0, 0]
        for v in range(j + 1, m):
            ml[0] += 1
            oval = int(ls[i][v])
            if oval >= val:
                break

        for v in range(j - 1, -1, -1):
            ml[1] += 1
            oval = int(ls[i][v])
            if oval >= val:
                break

        for v in range(i + 1, n):
            ml[2] += 1
            oval = int(ls[v][j])
            if oval >= val:
                break

        for v in range(i - 1, -1, -1):
            ml[3] += 1
            oval = int(ls[v][j])
            if oval >= val:
                break

        visible[i][j] = reduce(lambda a, b: a * b, ml, 1)

print(visible)
ans = max([max(v) for v in visible])
print(ans)
