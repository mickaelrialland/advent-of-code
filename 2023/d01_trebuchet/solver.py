"""
Author: Mickaël
Date: 01/12/2023

https://adventofcode.com/2023/day/1
"""
import time
from pathlib import Path
import re

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def main():
    print(f"Part 1: only digits > value={part_one()}")
    print(f"Part 2: spelled with letters > value={part_two()}")

def part_one():
    return sum(map(concat_first_and_last_digits, open(INPUT_FILE)))

def concat_first_and_last_digits(line):
    x = re.findall(r'(\d)', line)
    return int(x[0] + x[-1])

def part_two():
    return sum(map(extract_digits_with_spelled, open(INPUT_FILE)))
    
def extract_digits_with_spelled(line):
    for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
        line = line.replace(n, n + str(i+1) + n)
    return concat_first_and_last_digits(line)

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")