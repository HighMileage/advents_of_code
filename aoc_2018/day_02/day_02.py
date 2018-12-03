from itertools import groupby
import csv


def inputs():
    with open('input_02.txt', 'r') as input_file:
        for value in csv.reader(input_file):
            yield value[0]


def repeats_characters(string, appearances):
    id_list = list(string)
    id_list.sort()
    return appearances in [len(list(group)) for _, group in groupby(id_list)]

def main():
    two_repeats = sum([repeats_characters(box_id, 2) for box_id in inputs()])
    three_repeats = sum([repeats_characters(box_id, 3) for box_id in inputs()])

    return two_repeats * three_repeats

if __name__ == '__main__':
    checksum = main()
    print("Looks like your checksum is {}".format(checksum))
