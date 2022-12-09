with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

n = len(ls)
m = len(ls[0])

visible = [[1 for i in range(m)] for j in range(n)]
for i in range(n):
    mx = -1

    for j in range(m):
        v = int(ls[i][j])
        if v > mx:
            mx = v
            visible[i][j] = True

    mx = -1
    for j in range(m-1, -1, -1):
        v = int(ls[i][j])
        if v > mx:
            mx = v
            visible[i][j] = True


for i in range(m):
    mx = -1
    for j in range(n):
        v = int(ls[j][i])
        if v > mx:
            mx = v
            visible[j][i] = True

    mx = -1
    for j in range(n-1, -1, -1):
        v = int(ls[j][i])
        if v > mx:
            mx = v
            visible[j][i] = True

ans = max([max(v) for v in visible])
print(ans)