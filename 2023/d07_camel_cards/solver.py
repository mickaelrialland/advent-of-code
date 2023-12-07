"""
Author: Mickaël
Date: 07/12/2023

Solving https://adventofcode.com/2023/day/7
"""
import time
from pathlib import Path
import itertools
import collections

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input/input.txt")

HAND_TYPES = [
    lambda x, j: len(x) < 2,                                                # Only one value > five of a kind
    lambda x, j: max(x.values()) + j == 4,                                  # Max counter + nbjoker = 4 > four of a kind
    lambda x, j: (len(x) == 2 and 2 in x.values() and 3 in x.values())      # Counter contains 2 and 3 or 2 2 and one joker > full
    or (collections.Counter(x.values())[2] == 2 and j == 1),
    lambda x, j: (3 - j) in x.values(),                                     # Counter - nb joker exists > Three of a kind            
    lambda x, j: (2 in collections.Counter(x.values()) and collections.Counter(x.values())[2] == 2) # 2 2, or 1 2 and joker > two pair
    or (j > 0 and 2 in collections.Counter(x.values())),
    lambda x, j: (2 - j) in x.values(),                                     # One pair                
]

def solve(hands, with_joker = False) -> int:
    # [[five of a kind], [four a kind], ....]
    sorted_hands = [[] for _ in range(len(HAND_TYPES)+1)]   # +1 for high card combinaison
    # Cards order if joker > J=0
    cards_order = {
        v: i for i, v in enumerate("J23456789TQKA" if with_joker else "23456789TJQKA")
    }

    for hand, bid in hands:
        # '32T3K' will convert to ({'3': 2, '2': 1, 'T': 1, 'K': 1})
        # With a length of 2, we know it's four of a kind
        counter = collections.Counter(hand)
        jokers = 0
        # Getting numbers of Jokers and remove them to not be count as a card
        if with_joker:
            jokers = counter["J"]
            del counter["J"]

        # Getting hand index to stock in right index in sorted_hands
        i = next(
            (i for i, hand_type in enumerate(HAND_TYPES) if hand_type(counter, jokers)), len(HAND_TYPES)
        )
        sorted_hands[i].append((hand, bid))

    for i, v in enumerate(sorted_hands):
        sorted_hands[i] = sorted(v, key=lambda x: [cards_order[c] for c in x[0]])

    return sum(
        i * bid
        for i, (_, bid) in enumerate(
            itertools.chain.from_iterable(sorted_hands[::-1]), start=1
        )
    )

def main():
    datas = open(INPUT_FILE, mode="rt").read().strip()
    hands = [(a, int(b)) for x in datas.split("\n") for a, b in [x.split()]]

    print(f"Part 1: {solve(hands)}")
    print(f"Part 2: {solve(hands, True)}")

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")