# https://adventofcode.com/2021/day/18

import json
from dataclasses import dataclass

lines = []
with open('in.in', 'r') as f:
    for l in f.readlines():
        l = l.strip('\n')
        lines.append(json.loads(l))


@dataclass
class Node:
    v = None
    l = None
    r = None
    p = None
    is_l = False

    def __repr__(self):
        if self.v is not None:
            return str(self.v)
        else:
            return f'[{self.l}, {self.r}]'


def parse(val, p=None):
    res = Node()
    res.p = p

    if isinstance(val, int):
        res.v = val
    else:
        l, r = val
        res.l = parse(l, res)
        res.l.is_l = True
        res.r = parse(r, res)

    return res


def add_left(node: Node, val: int):
    while node and node.is_l:
        node = node.p

    if node is None or node.p is None:
        return

    node = node.p.l

    while node.v is None:
        node = node.r

    node.v += val


def add_right(node: Node, val: int):
    while node and not node.is_l:
        node = node.p

    if node is None or node.p is None:
        return

    node = node.p.r

    while node.v is None:
        node = node.l

    node.v += val


def explode(node: Node, d=0) -> bool:
    if d >= 4:
        if node.v is not None:
            return False

        add_left(node, node.l.v)
        add_right(node, node.r.v)
        node.v, node.l, node.r = 0, None, None
        return True

    if node.v is not None:
        return False
    else:
        do = explode(node.l, d + 1)
        if do:
            return do
        return explode(node.r, d + 1)


def split(node: Node) -> bool:
    if node.v is not None:
        if node.v >= 10:
            node.l = parse(node.v // 2, node)
            node.l.is_l = True
            node.r = parse(node.v - (node.v // 2), node)
            node.v = None
            return True
        else:
            return False
    else:
        do = split(node.l)
        if do:
            return do
        return split(node.r)


def reduce(node):
    while True:
        if explode(node):
            continue
        if split(node):
            continue
        break
    return node


def add(a: Node, b: Node):
    root = Node()
    root.l, root.r = a, b
    a.p = b.p = root
    a.is_l = True
    return reduce(root)


def magnitude(node: Node):
    if node.v is not None:
        return node.v

    return magnitude(node.l) * 3 + magnitude(node.r) * 2


cur = reduce(parse(lines[0]))
for l in lines[1:]:
    cur = add(cur, reduce(parse(l)))
print(f'Part 1: {magnitude(cur)}')

max_m = 0
for v in lines:
    for u in lines:
        if u == v:
            continue
        max_m = max(max_m, magnitude(add(reduce(parse(v)), reduce(parse(u)))))
print(f'Part 2: {max_m}')
