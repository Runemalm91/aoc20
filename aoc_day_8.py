#!/usr/bin/env python3
import sys


def check_instruction(instruction, value, row_to_operate, accumulator):
    if instruction == 'nop':
        row_to_operate += 1
    elif instruction == 'acc':
        accumulator += int(value)
        row_to_operate += 1
    elif instruction == 'jmp':
        row_to_operate += int(value)

    return (row_to_operate, accumulator)


def part_1(instructions):
    accumulator, _ = test_run(instructions)
    print(f'Part 1: Accumulator value: {accumulator}')

def test_run(instructions):
    accumulator = 0
    row_to_operate = 0
    visited_rows = []
    while row_to_operate < len(instructions):
        instruction, value = instructions[row_to_operate].split()

        if row_to_operate in visited_rows:
            return accumulator, False;

        visited_rows.append(row_to_operate)

        row_to_operate, accumulator = check_instruction(
            instruction, value, row_to_operate, accumulator)

    return accumulator, True


def swap_instruction(instruction):
    if instruction == 'nop':
        return 'jmp'
    elif instruction == 'jmp':
        return 'nop'
    else:
        return 'acc'


def part_2(instructions):
    row_to_reach = len(instructions)
    for i in range(row_to_reach):
        old_instruction, old_value = instructions[i].split()
        instructions[i] = " ".join([swap_instruction(old_instruction), old_value])

        accumulator, is_valid = test_run(instructions)

        if is_valid:
            print(f'Part 2: Accumulator value: {accumulator}')
            break

        instructions[i] = " ".join([old_instruction, old_value])


def main():
    with open("aoc_day_8_data.txt", "r") as f:
        instructions = f.readlines()
        part_1(instructions)
        part_2(instructions)


if __name__ == "__main__":
    sys.exit(main())
