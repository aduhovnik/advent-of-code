# https://adventofcode.com/2021/day/14

from collections import defaultdict

ins = []
with open('in.in', 'r') as f:
    p = list(f.readline().strip('\n'))
    f.readline()
    for l in f.readlines():
        l = l.strip('\n')
        ins.append(l.split(' -> '))

print(p)
print(ins)

pairs = defaultdict(int)
for i in range(1, len(p)):
    pairs[''.join((p[i-1], p[i]))] += 1

for it in range(40):
    new_pairs = defaultdict(int)
    for pp, count in pairs.items():
        found = False
        for a, b in ins:
            if a == pp:
                c1, c2 = a[0], a[1]
                found = True
                new_pairs[''.join((c1, b))] += count
                new_pairs[''.join((b, c2))] += count
        if not found:
            new_pairs[pp] += count

    pairs = new_pairs

    cnt = defaultdict(int)
    for pp, count in pairs.items():
        cnt[pp[0]] += count
        cnt[pp[1]] += count

    cnt[p[0]] = cnt[p[0]] + 1
    cnt[p[-1]] = cnt[p[-1]] + 1

    for k in cnt:
        cnt[k] = cnt[k] // 2
    mx = max(cnt.values())
    mn = min(cnt.values())

    print('Step: ', it, 'min: ', mn, 'max: ', mx)

    print(mx - mn)
