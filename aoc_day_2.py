#!/usr/bin/env python3
import sys
import re


def get_index_list(string, ch):
    return [i for i, letter in enumerate(string) if letter == ch]


def find_nof_occurences(string, ch):
    return len(get_index_list(string, ch))


def main():
    ########## PART 1 ##########
    pattern = re.compile(
        r'(?P<minx>(\d+))-(?P<maxx>(\d+)) (?P<letter>(\w)): (?P<pwd>(\w+))\n'
    )

    with open("aoc_day_2_data.txt", "r") as f:
        lines = f.readlines()

        valid_passwords = 0
        for line in lines:
            match = pattern.search(line)
            match_dict = match.groupdict()
            nof_occurences = find_nof_occurences(
                match_dict['pwd'], match_dict['letter']
            )
            min_x = int(match_dict['minx'])
            max_x = int(match_dict['maxx'])

            if min_x <= nof_occurences <= max_x:
                valid_passwords += 1

        print(f'Number of valid passwords: {valid_passwords}')

        ########## PART 2 ##########
        valid_passwords = 0
        for line in lines:
            match = pattern.search(line)
            match_dict = match.groupdict()
            index_list = get_index_list(
                match_dict['pwd'], match_dict['letter'])
            min_x = int(match_dict['minx']) - 1
            max_x = int(match_dict['maxx']) - 1

            a = min_x in index_list
            b = max_x in index_list
            if a ^ b:
                valid_passwords += 1

        print(f'Number of valid passwords: {valid_passwords}')


if __name__ == '__main__':
    sys.exit(main())
