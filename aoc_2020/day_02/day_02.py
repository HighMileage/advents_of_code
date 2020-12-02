import csv
import sys

def inputs(file_path):
    with open(file_path, "r") as input_file:
        for value in csv.reader(input_file):
            yield value[0]

def main(file_path):
    good = []
    for x in inputs(file_path):
        range_text, limit_letter, password = x.split(" ")
        limit_letter = limit_letter.replace(':', '')

        low = int(range_text.split("-")[0])
        high = int(range_text.split("-")[1])

        count = 0
        if password[low-1] == limit_letter:
            count=count+1

        if password[high-1] == limit_letter:
            count=count+1

        if count == 1:
            good.append(password)

        print(limit_letter, high, low, "-----", x)

    print(len(good))

if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 2: XXXXX --------------------- \n")
    main(input_file)
