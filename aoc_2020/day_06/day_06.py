"""Day 6"""
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    data = list(inputs(file_path))
    batch = ""
    responses = []
    for i, line in enumerate(data):
        batch = batch + line
        if i + 1 < len(data) and data[i + 1] == "":
            responses.append(batch)
            batch = ""
        if i + 1 == len(data):
            responses.append(batch)

    count = 0
    for response in responses:
        uniques = set()
        uniques.update(response)
        count += len(uniques)
        # print("".join(sorted(uniques)))
    print(f"Found {count} questions that had 'yes' responses")


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 6: Custom Customs --------------------- \n")
    main(input_file)
