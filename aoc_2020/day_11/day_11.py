"""Day 11"""
from aocd.models import Puzzle
from collections import Counter
import itertools
import io
import os
import sys
from collections import namedtuple

DAY = int(os.path.splitext(os.path.basename(__file__))[0].split("_")[1])
Seat = namedtuple("Seat", "x y")
EIGHT_OCCUPIED = """
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
"""

MULTI = """
.............
.L.L.#.#.#.#.
.............
"""


def process_data(input_data):
    return [list(line.strip()) for line in input_data]


def get_data(filepath=None):

    data = []
    if filepath:
        with open(filepath, "r") as input_file:
            for line in input_file.readlines():
                yield line.strip()
    else:
        puzzle = Puzzle(year=2020, day=DAY)
        data = io.StringIO(puzzle.input_data)

        for line in data.readlines():
            yield line.strip()


def main(data):
    d = process_data(data)
    # d = process_data(line for line in MULTI.strip().split("\n"))
    s = SeatingLayout(d)
    layout = ""
    while True:
        s.tick()
        # print(s.seating_layout(), "\n")
        if s.seating_layout() == layout:
            occupied_seats = sum(1 for seat in s.seating_layout() if seat == "#")
            print(f"We've stabilized with {occupied_seats} occupied seats!\n")
            # print(s.seating_layout())
            break
        layout = s.seating_layout()


class SeatingLayout:
    def __init__(self, seating):
        self.max_x = len(seating[0])
        self.max_y = len(seating)
        self.possible_xs = range(self.max_x)
        self.possible_ys = range(self.max_y)
        self.seating_data = seating
        self.next = [[None for x in self.possible_xs] for x in self.possible_ys]

    def surrounding_seats(self, seat):
        x, y = seat
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                neighbor_x = x + j
                neighbor_y = y + i

                if neighbor_x in self.possible_xs and neighbor_y in self.possible_ys:
                    yield (neighbor_x, neighbor_y)

    def line_of_sight_seats(self, seat):
        slopes = [
            slope
            for slope in [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
            if slope != (0, 0)
        ]

        seats = []
        x, y = seat

        for slope in slopes:
            run, rise = slope
            i = 1
            while True:
                try:
                    target_x = x + run * i
                    target_y = y + rise * i
                    # print(f"Processing ({target_x}, {target_y})")
                    i += 1
                    if (
                        (target := self.seating_data[target_y][target_x] in ("#", "L"))
                        and target_x >= 0
                        and target_y >= 0
                    ):
                        seats.append((target_x, target_y))
                        break

                except IndexError as e:
                    break

        return seats

    def empty_no_neighbors(self, seat):
        x, y = seat
        if self.seating_data[y][x] == "L":
            return all(
                not self.occupied(seat) for seat in self.line_of_sight_seats(seat)
            )
        return False

    def occupied_with_neighbors(self, seat):
        x, y = seat
        if self.seating_data[y][x] == "#":
            return (
                sum(1 for seat in self.line_of_sight_seats(seat) if self.occupied(seat))
                >= 5
            )
        return False

    def occupied(self, seat):
        x, y = seat
        return self.seating_data[y][x] == "#"

    def seating_layout(self):
        return "\n".join("".join(row) for row in self.seating_data)

    def tick(self):
        new_layout = []
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.seating_data[y][x] == ".":
                    self.next[y][x] = "."
                    continue

                if self.empty_no_neighbors((x, y)):
                    self.next[y][x] = "#"
                    continue

                if self.occupied_with_neighbors((x, y)):
                    self.next[y][x] = "L"
                    continue

                self.next[y][x] = self.seating_data[y][x]

        self.seating_data = self.next
        self.next = [[None for x in self.possible_xs] for x in self.possible_ys]


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) == 2 else None
    data = get_data(filepath)
    puzzle = Puzzle(year=2020, day=DAY)

    print(f"Day {DAY}: {puzzle.title} --------------------- \n")
    main(data)
