#!/usr/bin/env python3
import sys


def count_trees(slope, row_increase, col_increase):
    number_of_trees = 0
    col = 0
    for row in range(row_increase, len(slope), row_increase):
        col = (col + col_increase) % len(slope[row].strip('\n'))
        if slope[row][col] == '#':
            number_of_trees += 1

    return number_of_trees


def main():
    with open("aoc_day_3_data.txt", "r") as f:
        slope = f.readlines()

        ######## PART 1 ########
        number_of_trees = count_trees(slope, 1, 3)

        print(f'Number of trees {number_of_trees}')

        ######## PART 2 ########
        rows_to_check = [1, 1, 1, 1, 2]
        cols_to_check = [1, 3, 5, 7, 1]

        product = 1
        for row, col in zip(rows_to_check, cols_to_check):
            product *= count_trees(slope, row, col)
        print(f'Product of numbers {product}')


if __name__ == '__main__':
    sys.exit(main())
