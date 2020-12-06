#!/usr/bin/env python3
import sys


def main():
    from aoc_day_1_data import input

    ########## PART 1 ##########

    for i, val in enumerate(input):
        for j in range(i, len(input)):
            if val + input[j] == 2020:
                print(f'Part 1. The product is: {val * input[j]}')

    ########## PART 2 ##########
    import numpy as np
    for i, val in enumerate(input):
        i_sum = np.array(input) + val
        for j in range(i, len(input)):
            if (i_sum + input[j] == 2020).any():
                product = \
                    val * (i_sum[i_sum == (2020 - input[j])] - val) * input[j]
                print(f'Part 2. The product is: {product}')
                break


if __name__ == '__main__':
    sys.exit(main())
