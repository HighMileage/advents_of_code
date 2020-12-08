"""Day 7"""
import sys


def inputs(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def main(file_path):
    data = inputs(file_path)
    bag_rules = get_bag_rules(data)
    target_bag = "shiny gold"

    good_bags = list(
        bag for bag in bag_rules.keys() if can_contain_bag(bag, target_bag, bag_rules)
    )

    print(f"Found {len(good_bags)} bags that must contain {target_bag} bag")
    for b in good_bags:
        print("\t", b)

    total_bag_count = get_bag_count(target_bag, bag_rules)
    print(
        f"Total bag count within a shiny gold is {total_bag_count - 1}"
    )  # Minus one for outer most bag


def get_bag_count(bag_type, rules):

    eventually_singleton_bags = [bag_type]
    bags_with_contents = []

    while True:
        new_bags = []
        for bag in eventually_singleton_bags:
            if len(rules[bag]) == 0:
                new_bags.append(bag)
                continue

            bags_with_contents.append(bag)
            for b, count in rules[bag].items():
                for _ in range(0, int(count)):
                    new_bags.append(b)

        if new_bags == eventually_singleton_bags:
            break
        eventually_singleton_bags = new_bags

    return len(eventually_singleton_bags + bags_with_contents)


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
