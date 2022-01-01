# https://adventofcode.com/2021/day/23

from dataclasses import dataclass
from typing import List, Tuple

grid = []
with open('in.in', 'r') as f:
    for l in f.readlines():
        l = l.strip('\n')
        grid.append(list(l.ljust(13, '#').replace(' ', '#')))

COST = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

ORDER = ['A', 'B', 'C', 'D']
Q_ENTRIES = [2, 4, 6, 8]


@dataclass
class State:
    hall: List[str]
    queues: List[List[str]]

    def __hash__(self):
        return hash((tuple(self.hall), (tuple(v) for v in self.queues)))

    def __copy__(self):
        return State(self.hall[::], [v[::] for v in self.queues])

    def solved(self):
        for q_idx, q in enumerate(self.queues):
            if any(v != ORDER[q_idx] for v in q):
                return False
        return True


def can_insert_to_queue(queue: List[str], letter) -> bool:
    if queue.count('.') + queue.count(letter) == len(queue):
        return True
    return False


def can_move_from_queue_to_hall(state: State, q_idx: int, hall_idx: int) -> bool:
    if hall_idx in Q_ENTRIES:
        return False

    q_entry = Q_ENTRIES[q_idx]
    a = min(q_entry, hall_idx)
    b = max(q_entry, hall_idx)
    return all(v == '.' for v in state.hall[a:b + 1])


def can_enter_queue(state: State, q_idx: int, hall_idx: int) -> bool:
    q_entry = Q_ENTRIES[q_idx]
    a = min(q_entry, hall_idx)
    b = max(q_entry, hall_idx)
    for i in range(a, b + 1):
        if i == hall_idx:
            continue
        if state.hall[i] != '.':
            return False
    return True


def move_from_hall_to_queue(state: State, hall_idx: int) -> Tuple[State, int]:
    letter = state.hall[hall_idx]
    queue_idx = ORDER.index(letter)
    queue = state.queues[queue_idx]
    empty_queue_idx = len(queue) - 1
    while queue[empty_queue_idx] != '.':
        empty_queue_idx -= 1
    assert empty_queue_idx > -1

    new_state = state.__copy__()
    new_state.hall[hall_idx] = '.'
    new_state.queues[queue_idx][empty_queue_idx] = letter

    moves = abs(Q_ENTRIES[queue_idx] - hall_idx) + 1 + empty_queue_idx
    return new_state, moves


def should_move_out_of_queue(queue: List[str], q_idx: int) -> bool:
    letter = ORDER[q_idx]
    if queue.count('.') + queue.count(letter) == len(queue):
        return False
    return True


def move_from_queue(state: State, q_idx: int, hall_idx: int) -> Tuple[State, int]:
    queue = state.queues[q_idx]
    letter_q_idx = 0
    while queue[letter_q_idx] == '.':
        letter_q_idx += 1

    new_state = state.__copy__()
    new_state.hall[hall_idx] = queue[letter_q_idx]
    new_state.queues[q_idx][letter_q_idx] = '.'

    moves = abs(Q_ENTRIES[q_idx] - hall_idx) + 1 + letter_q_idx
    return new_state, moves


DP = dict()


def dfs(state: State, depth=0) -> int:
    if state in DP:
        return DP[state]

    if state.solved():
        DP[state] = 0
        return 0

    for hall_idx, letter in enumerate(state.hall):
        if letter == '.':
            continue

        q_idx = ORDER.index(letter)
        if can_enter_queue(state, q_idx, hall_idx) and can_insert_to_queue(state.queues[q_idx], letter):
            new_state, moves = move_from_hall_to_queue(state, hall_idx)
            new_cost = COST[letter] * moves
            ret = new_cost + dfs(new_state, depth + 1)
            DP[state] = ret
            return ret

    ans = 10 ** 10
    for q_idx, queue in enumerate(state.queues):
        if not should_move_out_of_queue(queue, q_idx):
            continue

        for hall_idx in range(len(state.hall)):
            if not can_move_from_queue_to_hall(state, q_idx, hall_idx):
                continue
            new_state, moves = move_from_queue(state, q_idx, hall_idx)
            letter = new_state.hall[hall_idx]
            new_cost = COST[letter] * moves
            ans = min(ans, dfs(new_state, depth + 1) + new_cost)

    return ans


if __name__ == '__main__':
    initial_state = State(
        hall=['.' for i in range(11)],
        queues=[[grid[x][y] for x in range(2, len(grid) - 1)] for y in [3, 5, 7, 9]]
    )

    print(initial_state)
    res = dfs(initial_state)
    print(f'Part 1: {res}')

    grid = grid[:3] + [
        list("###D#C#B#A###"),
        list("###D#B#A#C###"),
    ] + grid[3:]

    initial_state_p2 = State(
        hall=['.' for i in range(11)],
        queues=[[grid[x][y] for x in range(2, len(grid) - 1)] for y in [3, 5, 7, 9]]
    )
    print(initial_state_p2)
    res = dfs(initial_state_p2)
    print(f'Part 2: {res}')
