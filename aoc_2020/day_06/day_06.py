"""Day 6"""
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    data = inputs(file_path)
    group = []
    families = []

    for i, line in enumerate(data):
        if line == "":
            continue

        group.append(line)

        if i + 1 < len(data) and data[i + 1] == "":
            families.append(group)
            group = []

        if i + 1 == len(data):
            families.append(group)

    count = 0

    for family in families:
        commonalities = set()
        for i, member in enumerate(family):
            member_responses = set(member)

            if i == 0:
                commonalities = member_responses

            commonalities = commonalities & member_responses

        count += len(commonalities)

    print(f"Found {count} questions that had 'yes' reponses")


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 6: Custom Customs --------------------- \n")
    main(input_file)
