"""
Author: Mickaël
Date: 07/12/2023

Solving https://adventofcode.com/2023/day/7
"""
import time
from pathlib import Path
import re
import math

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

def parse_datas():
    instructions_string, nodes_string = open(INPUT_FILE, mode="rt").read().split("\n\n")
    # Convert LR.. on array of [0, 1,...]
    instructions = instructions_string.replace(
        'L', '0').replace('R', '1')
    instructions = [int(i) for i in instructions]

    nodes = {}
    for line in nodes_string.splitlines():
        p = re.findall(r"\w{3}", line)
        nodes[p[0]] = p[1:]

    return instructions, nodes

def part_one(instructions, nodes) -> int :
    total_steps = 0
    instruction_index = 0
    node = 'AAA'                # start from the AAA node

    while node != 'ZZZ':
        node = nodes[node][instructions[instruction_index]]
        total_steps += 1
        instruction_index += 1
        if instruction_index >= len(instructions):
            instruction_index = 0

    return total_steps

def part_two(instructions, nodes) -> int:
    total_steps_all_directions = []
    start_nodes = [k for k, v in nodes.items() if k[-1] == 'A']

    for node in start_nodes:
        instruction_index = 0
        total_steps = 0
        while node[-1] != 'Z':
            node = nodes[node][instructions[instruction_index]]
            total_steps += 1
            instruction_index += 1
            if instruction_index >= len(instructions):
                instruction_index = 0
        total_steps_all_directions.append(total_steps)

    total = total_steps_all_directions[0]
    for step in total_steps_all_directions[1:]:
        total = math.lcm(total, step)

    return total

def main():
    instructions, nodes = parse_datas()

    print(f"Part 1: {part_one(instructions, nodes)}")
    print(f"Part 2: {part_two(instructions, nodes)}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")