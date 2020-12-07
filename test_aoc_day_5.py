#!/usr/bin/env python3
import unittest
from aoc_day_5 import parse


class TestAOCDay5(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(70, parse("BFFFBBF", 'F', 'B', 0, 127))
        self.assertEqual(14, parse("FFFBBBF", 'F', 'B', 0, 127))
        self.assertEqual(102, parse("BBFFBBF", 'F', 'B', 0, 127))
        self.assertEqual(7, parse("RRR", 'L', 'R', 0, 7))
        self.assertEqual(7, parse("RRR", 'L', 'R', 0, 7))
        self.assertEqual(4, parse("RLL", 'L', 'R', 0, 7))
