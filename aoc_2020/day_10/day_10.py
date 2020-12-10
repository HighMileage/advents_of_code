"""Day 10"""
from aocd.models import Puzzle
from collections import Counter
import itertools
import io
import os
import sys

DAY = int(os.path.splitext(os.path.basename(__file__))[0].split("_")[1])


def process_data(input_data):
    return [int(line.strip()) for line in input_data]


def get_data(filepath=None):

    if filepath:
        with open(filepath, "r") as input_file:
            for line in input_file.readlines():
                yield line.strip()
    else:
        puzzle = Puzzle(year=2020, day=DAY)
        data = io.StringIO(puzzle.input_data)

        for line in data.readlines():
            yield line.strip()


def main(data):
    d = sorted(process_data(data))
    highest = int(d[-1]) + 3

    joltage_differences = []

    # Uncomment to visualize joltage diffs
    # print("0")
    for i, joltage in enumerate(d):
        if i == 0:
            difference = joltage - 0
        else:
            difference = joltage - d[i - 1]

        joltage_differences.append(difference)
        # Uncomment to visualize joltage diffs
        # print(f"---> {difference}")
        # print(joltage)

    # Uncomment to visualize joltage diffs
    # print(f"---> 3")
    # print(f"{highest}")

    joltage_differences.append(highest - d[-1])
    counts = Counter(joltage_differences)
    print(
        f"Looks like the 3 joltages {counts[3]} times the 1 joltages {counts[1]} would be {counts[1] * counts[3]}"
    )
    print(
        "Joltage difference fingerprint: ", "".join(str(i) for i in joltage_differences)
    )

    runs = []
    group = ""
    for diff in joltage_differences:
        if diff == 1:
            group += str(diff)
        else:
            if group not in ("1", ""):
                runs.append(group)
            group = ""

    diff_counts = Counter(runs)

    # It was easiest for me to think about how removing adapaters "condensed"
    # or spread joltage difference to a nearby neighbor. This joltage
    # difference condensing was only possible for consecutive neighbors that
    # were 1/2 jolts away from each other. Imagine the joltage adapaters below
    # and their corresponding joltage diffs:
    #     Joltages:        0, 1, 4, 5, 6, 7, 10
    #     Differences:       1  3  1  1  1  3

    # There are three ways to condense this plus the initial state, so 4 states overall.
    #     Joltages:        0, 1, 4, 6, 7, 10
    #     Joltages:        0, 1, 4, 5, 7, 10
    #     Joltages:        0, 1, 4, 7, 10
    #
    # The corresponding diff patterns:
    #     Joltages:        0, 1, 4, 6, 7, 10
    #     Differences:       1  3  2  1  3
    #
    #     Joltages:        0, 1, 4, 5, 7, 10
    #     Differences:       1  3  1  2  3
    #
    #     Joltages:        0, 1, 4, 7, 10
    #     Differences:       1  3  3  3
    #
    # Runs of 2 consecutive values can be represented by 2 unique joltage diff paterns
    # 11 --> Starting point
    # 2

    # Runs of 3 consecutive values can be represented by 4 unique joltage diff paterns
    # 1 1 1 --> Starting point
    # 1 2
    #   2 1
    #   3

    # Runs of 4 consecutive values can be represented by 7 unique joltage diff patterns
    #
    # 1 1 1 1 --> Starting point
    # 1  2  1 --> Condense from middle
    #  2  1 1 --> Condense from left
    #     3 1 --> Condense from left moar
    # 1 1  2  --> Condense from right
    # 1 3     --> Condense from right moar
    #  2   2  --> Condense from side centers

    total = 1
    run_type_combinations = {"11": 2, "111": 4, "1111": 7}

    print("Looks like there were several joltage diffs of 1 that could be condensed")
    for run_type, count in diff_counts.items():
        print(f"\t{count} runs of {len(run_type)} ({run_type})")
        total *= run_type_combinations[run_type] ** count

    print(f"Looks like there are {total} unique combinations, yowzas!")


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) == 2 else None
    data = get_data(filepath)
    puzzle = Puzzle(year=2020, day=DAY)

    print(f"Day {DAY}: {puzzle.title} --------------------- \n")
    main(data)
