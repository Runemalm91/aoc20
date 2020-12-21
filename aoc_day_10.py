#!/usr/bin/env python3
import sys
from math import factorial
import numpy as np


def compute_voltage_differenes(adapters):
    joltage_difference = np.diff(adapters)
    nof_one_joltage_diff = np.count_nonzero(joltage_difference == 1)
    nof_three_joltage_diff = np.count_nonzero(joltage_difference == 3)
    return (nof_one_joltage_diff, nof_three_joltage_diff)


def count_consecutive_ones(input):
    # We skip single ones, as they will not contribute any permutations
    consecutive_ones = []
    ones = 0
    for j in input:
        if j == 1:
            ones += 1
        else:
            if ones > 1:
                consecutive_ones.append(ones)
            ones = 0
    return consecutive_ones


def compute_valid_permutations(adapters):
    joltage_difference = np.diff(adapters)

    consecutive_ones = count_consecutive_ones(joltage_difference)

    def _cumsum(n):
        return np.cumsum(range(n+1))[n-1] + 1

    def _binomial_coefficient(n):
        return factorial(n) / (factorial(n - 2) * factorial(2)) + 1

    nof_valid_permutations = 1
    nof_valid_permutations2 = 1
    for n in consecutive_ones:
        nof_valid_permutations *= _cumsum(n)
        nof_valid_permutations2 *= _binomial_coefficient(n)

    return (nof_valid_permutations, nof_valid_permutations2)


def main():
    with open("aoc_day_10_data.txt", "r") as file:
        adapters = [int(line) for line in file]
        adapters.sort()
        adapters.insert(0, 0)  # Add charging outlet
        adapters.append(adapters[-1] + 3)  # Add built-in adapter

        nof_one_joltage_diff, nof_three_joltage_diff = \
            compute_voltage_differenes(adapters)
        print(f'Part 1: {nof_one_joltage_diff * nof_three_joltage_diff}')

        nof_valid_permutations, nof_valid_permutations2 = \
            compute_valid_permutations(adapters)

        print(f'Part 2 cumsum method: {nof_valid_permutations}')
        print(f'Part 2 binomial coefficient method: {nof_valid_permutations2}')


if __name__ == '__main__':
    sys.exit(main())
