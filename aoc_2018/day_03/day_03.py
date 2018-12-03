from itertools import groupby

def inputs():
    with open('input_03.txt', 'r') as input_file:
        contents = input_file.read().splitlines()
        for value in contents:
            yield _decode_row(value)


def _decode_row(row):
    claim_num = row.split('@')[0][1:].strip()
    _start_point, dim_string = row.split('@')[1].strip().split(':')
    start_point = tuple(int(point) for point in _start_point.split(','))
    x, y = dim_string.split('x')
    return (claim_num, start_point, (int(x), int(y)))


def get_impacted_points(claim):
    coordinates = []

    _claim_num, start_point, x_y_range = claim
    init_x = int(start_point[0])
    init_y = int(start_point[1])
    x_range, y_range = x_y_range

    for x_delta in range(1, x_range + 1):
        for y_delta in range(1, y_range + 1):
            coordinates.append((init_x + x_delta, init_y + y_delta))

    return coordinates


def main():
    all_coordinates = []
    for claim in inputs():
        all_coordinates += get_impacted_points(claim)

    all_coordinates.sort()
    number_of_doubles = sum(len(list(group)) >= 2 for coord, group in groupby(all_coordinates))
    print('Looks like there are at least {} spots with overlap of 2 or more claims'.format(number_of_doubles))

    singletons = set(coord for coord, group in groupby(all_coordinates) if len(list(group)) == 1)

    for claim in inputs():
        claim_set = set(get_impacted_points(claim))

        if singletons.intersection(claim_set) == claim_set:
            print('Found a claim that has no overlap: Claim #{}'.format(claim[0]))


if __name__ == '__main__':
    main()
