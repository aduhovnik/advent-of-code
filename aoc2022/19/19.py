# https://adventofcode.com/2022/day/19
import re
from functools import lru_cache

blueprints = []

with open('in.in', 'r') as f:
    for l in f.readlines():
        bid, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs = map(int, re.findall('(-?[0-9]+)', l.strip()))
        blueprints.append((bid, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs))


def run_simulation(blueprint, max_t=24, max_r=9):
    max_res = 0
    bid, ore_ore, clay_ore, obs_ore, obs_clay, geode_ore, geode_obs = blueprint

    @lru_cache(maxsize=None)
    def simulate(time=1, ore_r=1, clay_r=0, obs_r=0, geode_r=0, cur_ore=0, cur_clay=0, cur_obs=0, cur_geode=0):
        nonlocal max_res

        delta = max_t + 1 - time
        if max_res >= delta * (delta - 1) // 2 + cur_geode + delta * geode_r:
            # max res not achievable
            return 0

        # too many same robots
        if ore_r > max_r:
            return 0
        if clay_r > max_r:
            return 0
        if obs_r > max_r:
            return 0

        if time == max_t + 1:
            max_res = max(cur_geode, max_res)
            return cur_geode

        new_cur_ore = cur_ore + ore_r
        new_cur_clay = cur_clay + clay_r
        new_cur_obs = cur_obs + obs_r
        new_cur_geode = cur_geode + geode_r

        tans = 0

        MAX_ORE_TO_CREATE_ORE_R = 10
        MAX_CLAY_TO_CREATE_CLAY_R = 20
        MAX_OBS_TO_CREATE_OBS_R = 20

        # geode
        if cur_ore >= geode_ore and cur_obs >= geode_obs:
            tans = max(
                tans,
                simulate(time + 1, ore_r, clay_r, obs_r, geode_r + 1, new_cur_ore - geode_ore, new_cur_clay, new_cur_obs - geode_obs, new_cur_geode)
            )

        # obs
        if cur_ore >= obs_ore and cur_clay >= obs_clay and cur_obs < MAX_OBS_TO_CREATE_OBS_R:
            tans = max(
                tans,
                simulate(time + 1, ore_r, clay_r, obs_r + 1, geode_r, new_cur_ore - obs_ore, new_cur_clay - obs_clay, new_cur_obs, new_cur_geode)
            )

        # clay
        if cur_ore >= clay_ore and cur_clay < MAX_CLAY_TO_CREATE_CLAY_R:
            tans = max(
                tans,
                simulate(time + 1, ore_r, clay_r + 1, obs_r, geode_r, new_cur_ore - clay_ore, new_cur_clay, new_cur_obs, new_cur_geode)
            )

        # ore
        if ore_ore <= cur_ore < MAX_ORE_TO_CREATE_ORE_R:
            tans = max(
                tans,
                simulate(time + 1, ore_r + 1, clay_r, obs_r, geode_r, new_cur_ore - ore_ore, new_cur_clay, new_cur_obs, new_cur_geode)
            )

        tans = max(
            tans,
            simulate(time + 1, ore_r, clay_r, obs_r, geode_r, new_cur_ore, new_cur_clay, new_cur_obs, new_cur_geode)
        )
        return tans

    return simulate()


part1_ans = 0
for bl in blueprints:
    ans = run_simulation(bl, 24)
    print(ans)
    part1_ans += ans * bl[0]

print(f'part1: {part1_ans}')


part2_ans = 1
for bl in blueprints[:3]:
    ans = run_simulation(bl, 32)
    print(ans)
    part2_ans *= ans

print(f'part2: {part2_ans}')
