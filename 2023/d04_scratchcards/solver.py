"""
Author: Mickaël
Date: 04/12/2023

Solving https://adventofcode.com/2023/day/4
"""
import time
from pathlib import Path
import collections

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def part_one(line: str):
    x = 0
    winning_numbers, my_numbers = line.split("|")

    winning_set = set(winning_numbers.split())
    my_set = set(my_numbers.split())

    matches = len(winning_set & my_set)
    if matches>0:
        x = pow(2, matches-1)

    return x

def part_two(lines: str):
    scratchcards = 0
    scratchcard_points = collections.defaultdict(int)
    
    for i, line in enumerate(lines):
        scratchcard_points[i] += 1

        winning_numbers, my_numbers = line.split("|")

        winning_set = set(winning_numbers.split())
        my_set = set(my_numbers.split())

        for j in range(len(winning_set.intersection(my_set))):
            scratchcard_points[i + j + 1] += scratchcard_points[i]

        scratchcards += scratchcard_points[i]

    return scratchcards

def main():
    score = sum(map(part_one, open(INPUT_FILE, mode="rt")))
    count = part_two(open(INPUT_FILE, mode="rt"))
    print(f"Part 1: {score}")
    print(f"Part 2: {count}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")