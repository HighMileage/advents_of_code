"""Day 7"""
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    data = inputs(file_path)
    bag_rules = get_bag_rules(data)
    # print(bag_rules)

    good_bags = []
    for bag in bag_rules.keys():
        if can_contain_bag(bag, "shiny gold", bag_rules):
            good_bags.append(bag)

    print(f"Found {len(good_bags)} bag that will contain 'shiny gold' bags")
    for b in good_bags:
        print("\t", b)


def can_contain_bag(outer_bag, target_bag, rules):
    inner_bags = list(rules[outer_bag].keys())

    if target_bag in inner_bags:
        return True

    if len(inner_bags) == 0:
        return False

    return any(can_contain_bag(bag, target_bag, rules) for bag in inner_bags)


def get_bag_rules(data):
    bag_rules = {}
    for i, line in enumerate(data):
        outer_bag, inner_bags_string = line.replace(".", "").split(" bags contain ")
        inner_bags = inner_bags_string.split(", ")

        rules = {}
        for bag in inner_bags:
            count, bag_type = bag.split(" ", 1)
            cleaned_bag_type = bag_type.replace(" bags", "").replace(" bag", "")

            if count == "no":
                continue
            rules[cleaned_bag_type] = count
        bag_rules[outer_bag] = rules

    return bag_rules


if __name__ == "__main__":
    input_file = sys.argv[1]
    print("Day 6: XXX --------------------- \n")
    main(input_file)
