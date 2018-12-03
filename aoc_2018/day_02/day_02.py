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


def checksum():
    two_repeats = sum([repeats_characters(box_id, 2) for box_id in inputs()])
    three_repeats = sum([repeats_characters(box_id, 3) for box_id in inputs()])

    return two_repeats * three_repeats


def one_character_diff(target_id, base_id):
    return 1 == sum(target != base for target, base in zip(list(target_id), list(base_id)))


def compare_to_all_ids(candidate_id):
    for target_id in inputs():
        if one_character_diff(target_id, candidate_id):
            print('Found nearly matching ids:\n    {}\n    {}'.format(target_id, candidate_id))
            return (target_id, candidate_id)
    return None

def identify_correct_boxes():
    near_matches = None
    for candidate_id in inputs():
        near_matches = compare_to_all_ids(candidate_id)
        if near_matches:
            return near_matches

    return near_matches


if __name__ == '__main__':
    checksum = checksum()
    print("---------------------------PART 1---------------------------")
    print("Looks like your checksum is {}".format(checksum))

    print("\n---------------------------PART 2---------------------------")
    box_one_ids, box_two_ids = identify_correct_boxes()

    common_letters = ''.join(char_1 for char_1, char_2 in zip(box_one_ids, box_two_ids) if char_1 == char_2)
    print('Found these common charactes: {}'.format(common_letters))
