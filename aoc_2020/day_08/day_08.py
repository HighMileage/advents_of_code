"""Day 8"""
import sys
from time import sleep


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()

        data = []
        for line in lines:
            command, string_value = line.strip().split(" ")
            data.append([command, int(string_value)])
        return data


def part1(file_path):
    accumulator = 0
    index = 0
    seen = set()
    data = inputs(file_path)

    replaceables = []
    for i, command in enumerate(data):
        cmd, _ = command
        if cmd in ("jmp", "nop"):
            replaceables.append(i)

    for i in replaceables:
        data = inputs(file_path)
        accumulator = 0
        index = 0
        seen = set()

        c, v = data[i]
        if c == "jmp":
            data[i] = ["nop", v]
        if c == "nop":
            data[i] = ["jmp", v]

        while True:
            try:
                command, value = data[index]
            except IndexError as e:
                print("Hit the end of the list")
                print(accumulator)
                return

            if index in seen:
                # print(seen)
                # for i in seen:
                #     print(i, data[i])
                print(
                    f"Stopping as you've already seen {index} (accumulator value => {accumulator})"
                )
                break

            seen.add(index)

            if command == "nop":
                index += 1
                continue

            if command == "acc":
                accumulator += value
                index += 1
                continue

            if command == "jmp":
                index += value
                continue


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 8: XXX --------------------- \n")
    part1(input_file)
