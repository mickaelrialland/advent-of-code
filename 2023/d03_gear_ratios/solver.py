"""
Author: Mickaël
Date: 04/12/2023

Solving https://adventofcode.com/2023/day/3
"""
import time
from pathlib import Path
import re
import math

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def parse_datas(lines: str):
    numbers = {}
    symbols = {}
    idx_num = 0

    for r, line in enumerate(lines):
        line_numbers = re.sub(r"\D", " ", line).split()
        offset = 0
        for num in line_numbers:
            pos = line.index(num, offset)
            for step in range(len(num)):
                numbers[(r, pos + step)] = (int(num), idx_num)
            offset = pos + len(num)
            idx_num += 1

        line_syms = re.sub(r"[\d\.]", " ", line).split()
        offset = 0
        for sym in line_syms:
            pos = line.index(sym, offset)
            symbols[(r, pos)] = sym
            offset = pos + 1

    return numbers, symbols

def part_one(numbers, symbols):
    adjacent_nums = []

    for pos, symbol in symbols.items():
        row, col = pos
        adjacent_pos = [(row + x, col + y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
        #print(pos, adj_pos)
        adjacent_nums.extend([numbers[pos] for pos in adjacent_pos if pos in numbers])
        #print(adj_nums)

    return sum(item[0] for item in set(adjacent_nums))

def part_two(numbers, symbols):
    total = 0

    for pos, symbol in symbols.items():
        if symbol == "*":
            row, col = pos
            adjacent_pos = [(row + x, col + y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
            adjacent_nums = set([numbers[pos] for pos in adjacent_pos if pos in numbers])
            if len(adjacent_nums) == 2:
                total += math.prod([item[0] for item in adjacent_nums])

    return total

def main():
    numbers, symbols = parse_datas(open(INPUT_FILE, mode="rt"))
    print(f"Part 1: {part_one(numbers, symbols)}")
    print(f"Part 2: {part_two(numbers, symbols)}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")