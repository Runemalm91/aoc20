#!/usr/bin/env python3
import sys
from math import floor, ceil
import numpy


def parse(input, lower_id, upper_id, lower_bound, upper_bound):
    for letter in input:
        if lower_bound == upper_bound:
            return lower_bound
        elif (upper_bound - lower_bound) == 1:
            if letter == upper_id:
                return upper_bound
            elif letter == lower_id:
                return lower_bound

        new_value = (upper_bound - lower_bound) / 2
        if letter == upper_id:
            lower_bound = ceil(new_value) + lower_bound
        elif letter == lower_id:
            upper_bound = floor(new_value) + lower_bound


def main():
    with open("aoc_day_5_data.txt", "r") as f:
        seat_data_set = f.readlines()

        seat_ids = []
        for seat_data in seat_data_set:
            row = parse(seat_data[:7], 'F', 'B', 0, 127)
            col = parse(seat_data[7:], 'L', 'R', 0, 7)
            seat_ids.append(row * 8 + col)

        print(f'Part 1: {numpy.amax(seat_ids)}')

        seat_ids.sort()
        seat_ids = numpy.array(seat_ids)
        seat_diff = numpy.diff(seat_ids)
        indices = seat_diff == 2
        indices = numpy.append(indices, False)

        # Increment because the diff operator gets the index of the prior seat
        print(f'Part 2: {seat_ids[indices] + 1}')

if __name__ == '__main__':
    sys.exit(main())
