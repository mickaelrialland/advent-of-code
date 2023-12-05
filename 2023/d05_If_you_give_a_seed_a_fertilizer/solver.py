"""
Author: Mickaël
Date: 04/12/2023

Solving https://adventofcode.com/2023/day/4
"""
import time
from pathlib import Path
import functools

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def todo(val, m):
    _, *ranges = m.split('\n')
    for r in ranges:
        dst, src, n=map(int, r.split())
        if src <= val < src+n:
            return val-src+dst
    else: return val

def part_one(seeds, maps):
    return min(functools.reduce(todo, maps, int(s)) for s in seeds)

def part_two(seeds, maps):
    pairs = list(zip(seeds[::2], seeds[1::2]))
    locations = []

    # Pas optimisé du tout, à revoir !!!
    for start, length in pairs:
        seed_range = [*range(start, start+length,1)]
        locations.append(part_one(seed_range, maps))

    return min(locations)

def main():
    seeds, *maps = open(INPUT_FILE, mode="rt").read().split('\n\n')
    seeds = [int(x) for x in seeds.split()[1:]]

    print(f"Part 1: {part_one(seeds, maps)}")
    print(f"Part 2: {part_two(seeds, maps)}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")