"""
Author: Mickaël
Date: 06/12/2023

Solving https://adventofcode.com/2023/day/6
"""
import time
from pathlib import Path
import math

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def test(racetime: int, racedist: int):
    b1 = int((racetime + math.sqrt(pow(racetime, 2) - 4 * racedist))/2)
    b2 = int((racetime - math.sqrt(pow(racetime, 2) - 4 * racedist))/2)

    return b1 - b2

def winning_options(racetime: int, racedist: int) -> int:
    def iterate(arange):
        for n in arange:
            if (racetime - n) * n > racedist:
                return n
            
    return iterate(range(racetime - 1, 1, -1)) - iterate(range(1, racetime)) + 1

def part_one(races: list) -> int:
    return math.prod(winning_options(*d) for d in races)

def part_two(times: list, dists: list) -> int:
    racetime = int("".join(str(t) for t in times))
    racedist = int("".join(str(d) for d in dists))
    return test(racetime, racedist)

def main():
    lines = open(INPUT_FILE, mode="rt").read().strip().split('\n')
    times,records=[int(x)for x in lines[0].split(':')[1].split()],[int(x)for x in lines[1].split(':')[1].split()]

    print(f"Part 1: {part_one(list(zip(times, records)))}")
    print(f"Part 2: {part_two(times, records)}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")