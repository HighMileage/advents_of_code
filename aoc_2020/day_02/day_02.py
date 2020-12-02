import csv
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        for value in csv.reader(input_file):
            yield value[0]


def main(file_path):
    valid_passwords_part_1 = []
    valid_passwords_part_2 = []

    for line in inputs(file_path):
        range_text, limit_letter, password = line.split(" ")
        limit_letter = limit_letter.replace(":", "")

        low = int(range_text.split("-")[0])
        high = int(range_text.split("-")[1])

        count = sum([1 for letter in password if letter == limit_letter])
        if count >= low and count <= high:
            valid_passwords_part_1.append(password)

        low_index_present = password[low - 1] == limit_letter
        high_index_present = password[high - 1] == limit_letter
        letters_present = [low_index_present, high_index_present]

        if not all(letters_present) and any(letters_present):
            valid_passwords_part_2.append(password)

    print(f"Found {len(valid_passwords_part_1)} passwords for part 1")
    print(f"Found {len(valid_passwords_part_2)} passwords for part 2")


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 2: Password Philosophy --------------------- \n")
    main(input_file)
