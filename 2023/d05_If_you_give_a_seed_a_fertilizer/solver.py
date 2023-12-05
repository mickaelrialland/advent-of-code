"""
Author: Mickaël
Date: 05/12/2023

Solving https://adventofcode.com/2023/day/5
"""
import time
from pathlib import Path
import math

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def parse_datas():
    with open(INPUT_FILE, mode="rt") as f:
        datas = [x.strip('\n') for x in f.readlines()]

    seeds = [int(x) for x in datas[0].split(':')[1].split()]

    maps = []
    curr_map = []
    for d in datas[3:]:
        if d == '':
            continue
        if ':' in d:
            maps += [curr_map]
            curr_map = []
        else:
            curr_map += [tuple(int(x) for x in d.split(' '))]

    maps += [curr_map]
    return seeds, maps


def apply_maps(seed, maps):
    val = seed
    for map in maps:
        # ds = destination start
        # ss = source start
        # rl = range lenght
        for ds, ss, rl in map:
            if ss <= val < ss + rl:
                val = ds + (val - ss)
                break
    return val

def part_one(seeds, maps):
    seeds_location = {apply_maps(s, maps): s for s in seeds}
    return min(seeds_location.keys())

def part_two(seeds, maps):
    seeds = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2)]

    step_size = int(pow(10, math.ceil(math.log10(max(s[1] for s in seeds) / 100))))
    search_vals = {(ss, ss + sl, s): apply_maps(s, maps) for ss, sl in seeds for s in range(ss, ss + sl, step_size)}
    rough_est = min(search_vals.items(), key = lambda x: x[1])

    seed_range_start, seed_range_end, best_est = rough_est[0]

    while step_size > 1:
        left_search  = max(best_est - step_size, seed_range_start)
        right_search = min(best_est + step_size, seed_range_end)

        step_size = step_size // 10
        search_vals = {s: apply_maps(s, maps) for s in range(left_search, right_search, step_size)}
        best_est, best_loc = min(search_vals.items(), key = lambda x: x[1])
    
    return best_loc

def main():
    seeds, maps = parse_datas()
    print(f"Part 1: {part_one(seeds, maps)}")
    print(f"Part 2: {part_two(seeds, maps)}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")