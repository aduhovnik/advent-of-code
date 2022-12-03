# https://adventofcode.com/2022/day/1

res = []
cur = 0
with open('in.in', 'r') as f:
    for l in f.readlines():
        l = l.strip()
        if len(l) == 0:
            res.append(cur)
            cur = 0
        else:
            cur += int(l)

res.append(cur)
# part 1
print(max(res))
# part 2
res.sort(reverse=True)
print(sum(res[:3]))
