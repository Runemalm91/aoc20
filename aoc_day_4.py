#!/usr/bin/env python3
import sys
import re


def parse_passport(info, passport_candidate):
    for part in info:
        key, value = part.split(":")
        passport_candidate[key] = value


def validate_passport(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for required_field in required_fields:
        if required_field not in passport.keys():
            return False
    return True


def validate_passort_part_2(passport):
    validation = {
        'byr': [1920, 2002],
        'iyr': [2010, 2020],
        'eyr': [2020, 2030],
        'hgt': {'cm': [150, 193], 'in': [59, 76]},
        'hcl': re.compile(r'^#[0-9,a-f]{6}$'),
        'ecl': ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        'pid': re.compile(r'^[0-9]{9}$')
    }

    def _is_within_bounds(input, min_val, max_val):
        return min_val <= int(input) <= max_val

    for key, value in validation.items():
        passport_val = passport[key]
        if isinstance(value, list):
            if not passport_val.isdigit():
                return False
            if not _is_within_bounds(passport_val, value[0], value[1]):
                return False
        elif isinstance(value, dict):
            if 'cm' in passport_val:
                if not _is_within_bounds(passport_val.rstrip('cm'), value['cm'][0], value['cm'][1]):
                    return False
            elif 'in' in passport_val:
                if not _is_within_bounds(passport_val.rstrip('in'), value['in'][0], value['in'][1]):
                    return False
            else:
                return False
        elif isinstance(value, tuple):
            if passport_val not in value:
                return False
        else:
            if value.search(passport_val) is None:
                return False

    return True


def main():
    with open("aoc_day_4_data.txt", "r") as f:
        batch_file = f.readlines()

        nof_valid_passports_1 = 0
        nof_valid_passports_2 = 0

        passport_candidate = {}
        for potential_passport in batch_file:
            partial_passport = potential_passport.strip('\n').split(' ')
            if not partial_passport[0]:
                #print(passport_candidate)
                is_valid_passport = validate_passport(passport_candidate)
                if is_valid_passport:
                    nof_valid_passports_1 += 1
                    is_valid_passport = validate_passort_part_2(
                        passport_candidate
                    )
                    if is_valid_passport:
                        nof_valid_passports_2 += 1
                        #print('Is valid')
                passport_candidate = {}
            else:
                parse_passport(partial_passport, passport_candidate)
        #print(passport_candidate)
        is_valid_passport = validate_passport(passport_candidate)
        if is_valid_passport:
            nof_valid_passports_1 += 1
            is_valid_passport = validate_passort_part_2(passport_candidate)
            if is_valid_passport:
                nof_valid_passports_2 += 1
                print('Is valid')

        print(f'Number of valid passports part 1 : {nof_valid_passports_1}')
        print(f'Number of valid passports part 2 : {nof_valid_passports_2}')


if __name__ == '__main__':
    sys.exit(main())
