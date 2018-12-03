from itertools import groupby

def inputs():
    with open('input_03.txt', 'r') as input_file:
        contents = input_file.read().splitlines()
        for value in contents:
            yield _decode_row(value)


def _decode_row(row):
    start_point, dim_string = row.split('@')[1].strip().split(':')
    x, y = dim_string.split('x')
    return (start_point, (int(x), int(y)))


def get_impacted_points(claim):
    coordinates = []

    init_x = int(claim[0].split(',')[0])
    init_y = int(claim[0].split(',')[1])
    x_range, y_range = claim[1]

    for x_delta in range(1, x_range + 1):
        for y_delta in range(1, y_range + 1):
            coordinates.append((init_x + x_delta, init_y + y_delta))

    return coordinates

def count_doubles():
    all_coordinates = []
    for claim in inputs():
        all_coordinates += get_impacted_points(claim)

    all_coordinates.sort()
    print('Here are the doubles')
    number_of_doubles = sum(len(list(group)) >= 2 for coord, group in groupby(all_coordinates))
    print(number_of_doubles)


if __name__ == '__main__':
    count_doubles()
