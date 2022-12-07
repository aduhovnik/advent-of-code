ls = []
with open('in.in', 'r') as f:
    ls = [l.strip() for l in f.readlines()]

assert (ls[0] == '$ cd /')

file_tree = {'/': dict()}

ptr = 0
cur_dir = ['/']


# traverse filesystem
def find_dir():
    res = file_tree
    for k in cur_dir[:-1]:
        res = res[k]
    return res


# build filesystem
while ptr < len(ls):
    if ls[ptr].startswith('$'):
        cmds = ls[ptr].split()
        if cmds[1] == 'ls':
            content = dict()
            while ptr + 1 < len(ls) and not ls[ptr + 1].startswith('$'):
                ptr += 1
                a, b = ls[ptr].split()
                if a == 'dir':
                    content[b] = dict()
                else:
                    content[b] = int(a)

            find_dir()[cur_dir[-1]] = content
        elif cmds[1] == 'cd':
            _, cd, where = cmds
            if where == '..':
                cur_dir = cur_dir[:-1]
            else:
                cur_dir = cur_dir + [where]

        ptr += 1


weights = []

# calculate total size
def dfs(content):
    s = 0
    for c, v in content.items():
        if type(v) == dict:
            s += dfs(v)
        else:
            s += v
    weights.append(s)
    return s


dfs(file_tree['/'])

# part 1
ans = sum(v for v in weights if v < 100000)
print(ans)

weights.sort()

# find dir to delete, part 2
total_sum = max(weights)
for v in weights:
    if 70000000 - total_sum + v > 30000000:
        print(v)
        break
