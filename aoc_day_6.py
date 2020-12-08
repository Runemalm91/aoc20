#!/usr/bin/env python3
import sys


def main():
    with open("aoc_day_6_data.txt", "r") as f:
        input_data = f.readlines()

        ctr = 0
        groups_1 = {ctr: []}
        groups_2 = {ctr: []}
        for person in input_data:
            if person.strip("\n"):
                groups_1[ctr].extend(person.strip("\n"))
                groups_2[ctr].append(person.strip("\n"))
            else:
                ctr += 1
                groups_1[ctr] = []
                groups_2[ctr] = []

        sum_part_1 = 0
        sum_part_2 = 0
        for group1, group2 in zip(groups_1.values(), groups_2.values()):
            sum_part_1 += len(set(group1))
            for unique_letter in set(group1):
                if all(unique_letter in person for person in group2):
                    sum_part_2 += 1
        print(f'Part 1 sum: {sum_part_1}')
        print(f'Part 2 sum: {sum_part_2}')

if __name__ == '__main__':
    sys.exit(main())
