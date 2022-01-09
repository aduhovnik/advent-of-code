m = []
with open('in.in', 'r') as f:
    for l in f.readlines():
        l = l.strip('\n')
        m.append(list(l))

for l in m:
    print(''.join(l))

for step in range(500):
    print(step)
    was_move = False
    n = len(m)
    mm = len(m[0])
    _m = [['.' for _ in range(mm)] for j in range(n)]
    for i in range(n):
        for j in range(mm):
            if m[i][j] == '>':
                ni = i
                nj = (j + 1) % mm
                if m[ni][nj] == '.':
                    _m[ni][nj] = '>'
                    was_move = True
                else:
                    _m[i][j] = '>'
            elif m[i][j] == 'v':
                _m[i][j] = m[i][j]
    m = _m
    _m = [['.' for _ in range(mm)] for j in range(n)]
    for i in range(n):
        for j in range(mm):
            if m[i][j] == 'v':
                ni = (i + 1) % n
                nj = j
                if m[ni][nj] == '.':
                    _m[ni][nj] = 'v'
                    was_move = True
                else:
                    _m[i][j] = 'v'
            elif m[i][j] == '>':
                _m[i][j] = m[i][j]
    m = _m
    if not was_move:
        break

    for l in m:
        print(''.join(l))

print(step+1)