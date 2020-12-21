#!/usr/bin/env python3
import unittest
import copy
from aoc_day_11 import (iterate_seats,
                        count_occupied_seats,
                        criteria_part_one,
                        criteria_part_two)


class TestAOCDay11(unittest.TestCase):
    """Unittest for day 11."""

    def setUp(self):
        self.start_seats = ['L.LL.LL.LL',
                            'LLLLLLL.LL',
                            'L.L.L..L..',
                            'LLLL.LL.LL',
                            'L.LL.LL.LL',
                            'L.LLLLL.LL',
                            '..L.L.....',
                            'LLLLLLLLLL',
                            'L.LLLLLL.L',
                            'L.LLLLL.LL']

    def test_iterate_seats_part_one(self):
        expected_seats = ['#.#L.L#.##',
                          '#LLL#LL.L#',
                          'L.#.L..#..',
                          '#L##.##.L#',
                          '#.#L.LL.LL',
                          '#.#L#L#.##',
                          '..L.L.....',
                          '#L#L##L#L#',
                          '#.LLLLLL.L',
                          '#.#L#L#.##']
        seats = copy.copy(self.start_seats)
        for _ in range(0, 5):
            seats = iterate_seats(seats, criteria_part_one)

        self.assertEqual(37, count_occupied_seats(seats))
        self.assertEqual(expected_seats, seats)

    def test_iterate_seats_part_two(self):
        expected_seats = ['#.L#.L#.L#',
                          '#LLLLLL.LL',
                          'L.L.L..#..',
                          '##L#.#L.L#',
                          'L.L#.LL.L#',
                          '#.LLLL#.LL',
                          '..#.L.....',
                          'LLL###LLL#',
                          '#.LLLLL#.L',
                          '#.L#LL#.L#']
        seats = copy.copy(self.start_seats)
        for _ in range(0, 6):
            seats = iterate_seats(seats, criteria_part_two)

        self.assertEqual(26, count_occupied_seats(seats))
        self.assertEqual(expected_seats, seats)
