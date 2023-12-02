"""
Author: Mickaël
Date: 02/12/2023

Solving https://adventofcode.com/2023/day/2
"""
import time
from pathlib import Path
import re
import collections
import math

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

COLORS = {"red": 12, "green": 13, "blue": 14}

def check_if_game_possible(line: str):
    game_id = int(line.split(":")[0].split()[-1])
    for color, max in COLORS.items():
        matches = re.findall(r"\d+ {}".format(color), line)
        if any(int(m.split()[0]) > max for m in matches):
            #print(game_id, "KO")
            return 0
    #print(game_id, "OK")
    return game_id

"""
As you continue your walk, the Elf poses a second question: in each game you played, 
what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
"""
def calculate_game_value(line: str):
    cubes = collections.defaultdict(int)   # not {} else cubes['red'] error if not initialized
    for color in COLORS:
        matches = re.findall(r"\d+ {}".format(color), line)
        for color_value in matches:
            # getting max number by color
            cubes[color] = max(cubes[color], int(color_value.split()[0]))
    return math.prod(cubes.values())

def main():
    game_one = sum(map(check_if_game_possible, open(INPUT_FILE, mode="rt")))
    game_two = sum(map(calculate_game_value, open(INPUT_FILE, mode="rt")))

    print(f"Part 1: {game_one}")
    print(f"Part 2: {game_two}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")