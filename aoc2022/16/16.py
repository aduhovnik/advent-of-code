# https://adventofcode.com/2022/day/16
import re
from functools import lru_cache

MAX_MINUTES = 30

rates = dict()
neighbours = dict()
with open("in.in", "r") as f:
    for l in f.readlines():
        l = l.strip()
        if not l: continue
        rate, = map(int, re.findall('=(-?[0-9]+)', l))
        valve, *neighs = re.findall('[A-Z]{2}', l)
        rates[valve] = rate
        neighbours[valve] = neighs

valves = list(neighbours.keys())
non_zero_valves = [v for v in valves if rates[v] > 0]

dist = {v: {u: float('inf') for u in valves} for v in valves}
for v in valves:
    dist[v][v] = 0

for v, neighs in neighbours.items():
    for u in neighs:
        dist[v][u] = 1
        dist[u][v] = 1

for k in valves:
    for i in valves:
        for j in valves:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

part1_answer = 0
visited_valves = 0


@lru_cache(maxsize=None)
def solve1(cur_valve='AA', minute=0, cur_ans=0):
    global part1_answer, visited_valves
    if minute > MAX_MINUTES:
        return

    part1_answer = max(cur_ans, part1_answer)

    for idx, v in enumerate(non_zero_valves):

        if visited_valves & (1 << idx):
            continue

        visited_valves ^= (1 << idx)

        new_minute = minute + dist[cur_valve][v] + 1
        delta = MAX_MINUTES - new_minute
        solve1(v, new_minute, cur_ans + rates[v] * delta)

        visited_valves ^= (1 << idx)


solve1()
print(f'part1: {part1_answer}')

part2_answer = 0
visited_by_me, visited_by_elephant = 0, 0


@lru_cache(maxsize=None)
def solve2(cur_me='AA', cur_elephant='AA', my_minute=4, elephant_minute=4, cur_ans=0):
    global part2_answer, visited_by_me, visited_by_elephant
    if my_minute > MAX_MINUTES or elephant_minute > MAX_MINUTES:
        return

    if part2_answer < cur_ans:
        print(cur_ans)

    part2_answer = max(cur_ans, part2_answer)

    if my_minute >= MAX_MINUTES or elephant_minute >= MAX_MINUTES:
        return

    for idx, v in enumerate(non_zero_valves):

        if visited_by_me & (1 << idx):
            continue

        if visited_by_elephant & (1 << idx):
            continue

        # me
        visited_by_me ^= (1 << idx)

        new_minute = my_minute + dist[cur_me][v] + 1
        if new_minute <= MAX_MINUTES:
            delta = MAX_MINUTES - new_minute
            solve2(v, cur_elephant, new_minute, elephant_minute, cur_ans + rates[v] * delta)

        visited_by_me ^= (1 << idx)

        # elephant
        visited_by_elephant ^= (1 << idx)

        new_minute = elephant_minute + dist[cur_elephant][v] + 1
        if new_minute <= MAX_MINUTES:
            delta = MAX_MINUTES - new_minute
            solve2(cur_me, v, my_minute, new_minute, cur_ans + rates[v] * delta)

        visited_by_elephant ^= (1 << idx)


solve2()
print(f'part2: {part2_answer}')
