#!/usr/bin/env python3
import sys
import numpy as np


def find_invalid_number(numbers):
    preamble_length = 25
    preamble = []
    for i in range(preamble_length):
        preamble.append(numbers[i])

    for number in numbers[preamble_length:]:
        preamble_matrix = np.zeros((preamble_length, preamble_length))
        for i in range(preamble_length):
            preamble_matrix[i, :] = preamble
            preamble_matrix[i, :] += preamble[i]
            preamble_matrix[i, i] = np.nan  # Invalidate main diagonal

        if number not in preamble_matrix:
            return number

        preamble.pop(0)
        preamble.append(number)

def find_encryption_weakness(numbers, target):
    l = 0
    h = 0
    while h < len(numbers):
        sum = np.sum(numbers[l:h+1])
        if sum == target:
            break
        elif sum > target:
            l += 1
            h = l
        else:
            h += 1

    return min(numbers[l:h+1]) + max(numbers[l:h+1])


def main():
    with open("aoc_day_9_data.txt", "r") as file:
        numbers = [int(line) for line in file]

        invalid_number = find_invalid_number(numbers)
        print(f'Invalid number: {invalid_number}')

        encryption_weakness = find_encryption_weakness(numbers, invalid_number)
        print(f'Encryption weakness: {encryption_weakness}')


if __name__ == '__main__':
    sys.exit(main())
