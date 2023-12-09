"""
Author: Mickaël
Date: 09/12/2023

Solving https://adventofcode.com/2023/day/9
"""
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def compute(report_line: list) -> int:
    total = 0
    while any(report_line):
        total += report_line[-1]
        report_line = [report_line[i+1]-report_line[i] for i in range(len(report_line)-1)]
        #print(report_line, total)
    return total

def part_one(report_values: list) -> int :
    return sum(compute(report_line) for report_line in report_values)

def part_two(report_values: list) -> int:
    return sum(compute(report_line[::-1]) for report_line in report_values)

def main():
    report_values = [list(map(int, line.split())) for line in open(INPUT_FILE)]
    print(f"Part 1: {part_one(report_values)}")
    print(f"Part 2: {part_two(report_values)}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")