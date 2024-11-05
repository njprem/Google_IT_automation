#!/usr/bin/env python3
import unittest
from re_script import rearange_name

class test_rearrange_name(unittest.TestCase):

    def test_script(self):
        testcase = "Jaroenchokwittaya, Nutthawut"
        expected = "Nutthawut, Jaroenchokwittaya"
        self.assertEqual(rearange_name(testcase), expected)

if __name__ == "__main__":
    unittest.main()