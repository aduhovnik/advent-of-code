# https://adventofcode.com/2021/day/12

from collections import defaultdict

edges = []
with open('in.in', 'r') as f:
    for l in f.readlines():
        a, b = l.strip('\n').split('-')
        edges.append((a, b))

print(edges)

g = defaultdict(list)
for u, v in edges:
    g[u].append(v)
    g[v].append(u)

print(g)

u_routes = set()


def dfs(v, path=None):
    if path is None:
        path = []
    path.append(v)
    if v == 'end':
        u_routes.add('.'.join(path))
        return

    for u in g[v]:
        if u.isupper():
            dfs(u, path[::])
        else:
            if u in ('start', 'end'):
                if u in path:
                    continue
            if u in path:
                counts = defaultdict(int)
                for i in path:
                    if i.islower():
                        counts[i] += 1

                if 2 in counts.values():
                    continue
                else:
                    dfs(u, path[::])
                continue
            else:
                dfs(u, path[::])


dfs('start')
print(u_routes)
print('Part 2: ', len(u_routes))
