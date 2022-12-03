# https://adventofcode.com/2022/day/3

ls = []
with open('in.in', 'r') as f:
    for l in f.readlines():
        l = l.strip()
        ls.append(l)

ans = 0
for l in ls:
    fh = set(l[:len(l) // 2])
    sh = set(l[len(l) // 2:])
    c = fh & sh
    assert(len(c) == 1)
    ch = list(c)[0]
    if ord('a') <= ord(ch) <= ord('z'):
        ans += ord(ch) - ord('a') + 1
    else:
        ans += ord(ch) - ord('A') + 27

# part1
print(ans)

ans = 0
for i in range(0, len(ls), 3):
    s1, s2, s3 = ls[i:i+3]
    c = set(s1) & set(s2) & set(s3)
    assert(len(c) == 1)
    ch = list(c)[0]
    if ord('a') <= ord(ch) <= ord('z'):
        ans += ord(ch) - ord('a') + 1
    else:
        ans += ord(ch) - ord('A') + 27

# part2
print(ans)
