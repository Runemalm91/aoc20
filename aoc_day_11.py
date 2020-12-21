#!/usr/bin/env python3
import sys
import copy

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1),
              (1, 1), (-1, -1), (1, -1), (-1, 1)]


def _get_surrounding_area(seats, row, col):
    relative_start_row = -1 if row > 0 else 0
    relative_end_row = 2 if row+1 < len(seats) else 1
    area = []
    c_min = max(col-1, 0)
    c_max = min(col+2, len(seats[row]))
    for relative_row in range(relative_start_row, relative_end_row):
        area.append(seats[row+relative_row][c_min:c_max])
    return area


def count_occupied_seats(area):
    seat_count = 0
    for row in area:
        seat_count += row.count('#')
    return seat_count


def _replace_string(old_string, letter, loc):
    return old_string[0:loc] + letter + old_string[loc+1:]

def _check_seat_criteria(seats, row, col, area, new_seats):
    if seats[row][col] == 'L' and count_occupied_seats(area) == 0:
        new_seats[row] = _replace_string(new_seats[row], '#', col)
    elif seats[row][col] == '#' and count_occupied_seats(area) > 4:
        new_seats[row] = _replace_string(new_seats[row], 'L', col)


def criteria_part_one(seats, row, col, new_seats):
    area = _get_surrounding_area(seats, row, col)
    _check_seat_criteria(seats, row, col, area, new_seats)


def criteria_part_two(seats, row, col, new_seats):
    area = []
    if seats[row][col] != '.':
        for row_mod, col_mod in DIRECTIONS:
            new_row = row + row_mod
            new_col = col + col_mod

            while (0 <= new_row < len(seats)) and (
                    0 <= new_col < len(seats[new_row])):
                if seats[new_row][new_col] in 'L#':
                    area.append(seats[new_row][new_col])
                    break
                new_row += row_mod
                new_col += col_mod

        _check_seat_criteria(seats, row, col, area, new_seats)


def iterate_seats(seats, criteria_function):
    new_seats = copy.copy(seats)

    for row in range(len(seats)):
        for col in range(len(seats[row])):
            criteria_function(seats, row, col, new_seats)

    return new_seats


def main():
    with open("aoc_day_11_data.txt", "r") as file:
        original_seats = [row.strip('\n') for row in file]

        seats = copy.copy(original_seats)
        old_seats = None
        while seats != old_seats:
            old_seats = seats
            seats = iterate_seats(old_seats, criteria_part_one)
        print(
            f'Part 1: Number of occupied seats: {count_occupied_seats(seats)}')

        seats = copy.copy(original_seats)
        old_seats = None
        while seats != old_seats:
            old_seats = seats
            seats = iterate_seats(old_seats, criteria_part_two)
        print(
            f'Part 2: Number of occupied seats: {count_occupied_seats(seats)}')


if __name__ == '__main__':
    sys.exit(main())
