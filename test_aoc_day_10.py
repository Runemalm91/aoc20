#!/usr/bin/env python3
import unittest
from aoc_day_10 import compute_voltage_differenes, compute_valid_permutations


class TestAOCDay10(unittest.TestCase):
    """Unittest for day 10."""

    def setUp(self):
        self.test_adapters_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.test_adapters_1.sort()
        self.test_adapters_1.insert(0, 0)  # Add charging outlet
        self.test_adapters_1.append(
            self.test_adapters_1[-1] + 3)  # Add built-in adapter

        self.test_adapters_2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
                                38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        self.test_adapters_2.sort()
        self.test_adapters_2.insert(0, 0)  # Add charging outlet
        self.test_adapters_2.append(
            self.test_adapters_2[-1] + 3)  # Add built-in adapter

    def test_compute_voltage_differenes(self):
        nof_one_joltage_diff, nof_three_joltage_diff = \
            compute_voltage_differenes(self.test_adapters_1)

        self.assertEqual(35, nof_one_joltage_diff * nof_three_joltage_diff)

        nof_one_joltage_diff, nof_three_joltage_diff = \
            compute_voltage_differenes(self.test_adapters_2)

        self.assertEqual(220, nof_one_joltage_diff * nof_three_joltage_diff)

    def test_compute_valid_permutations(self):
        nof_valid_permutations, nof_valid_permutations2 = \
            compute_valid_permutations(self.test_adapters_1)
        self.assertEqual(8, nof_valid_permutations)
        self.assertEqual(8, nof_valid_permutations2)

        nof_valid_permutations, nof_valid_permutations2 = \
            compute_valid_permutations(self.test_adapters_2)

        self.assertEqual(19208, nof_valid_permutations)
        self.assertEqual(19208, nof_valid_permutations2)
