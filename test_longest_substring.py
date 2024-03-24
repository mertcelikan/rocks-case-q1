#!/usr/bin/env python3
import unittest
from solution import LongestSubstringFinder


class TestLongestSubstringFinder(unittest.TestCase):
    def test_single_longest_substring(self):
        input_string = "ABBCDDEFGHII"
        expected_output = [(6, ['DEFGHI'])]
        length, substrings = LongestSubstringFinder.find_longest_substring(input_string)
        self.assertEqual(length, expected_output[0][0])
        self.assertIn(substrings[0], expected_output[0][1])

    def test_multiple_longest_substrings(self):
        input_string = "AABBCCD"
        expected_output = [(2, ['AB', 'BC', 'CD'])]
        length, substrings = LongestSubstringFinder.find_longest_substring(input_string)
        self.assertEqual(length, expected_output[0][0])
        for substring in substrings:
            self.assertIn(substring, expected_output[0][1])

    def test_no_duplicate_characters(self):
        input_string = "ABCD"
        expected_output = [(4, ['ABCD'])]
        length, substrings = LongestSubstringFinder.find_longest_substring(input_string)
        self.assertEqual(length, expected_output[0][0])
        self.assertIn(substrings[0], expected_output[0][1])

    def test_empty_string(self):
        input_string = ""
        expected_output = [(0, [])]
        length, substrings = LongestSubstringFinder.find_longest_substring(input_string)
        self.assertEqual(length, expected_output[0][0])
        self.assertEqual(substrings, expected_output[0][1])

    def test_all_characters_are_duplicates(self):
        input_string = "AAAAA"
        expected_output = [(1, ['A'])]
        length, substrings = LongestSubstringFinder.find_longest_substring(input_string)
        self.assertEqual(length, expected_output[0][0])
        self.assertEqual(substrings, expected_output[0][1])

    def test_all_characters_are_unique(self):
        input_string = "ABCDEFG"
        expected_output = [(7, ['ABCDEFG'])]
        length, substrings = LongestSubstringFinder.find_longest_substring(input_string)
        self.assertEqual(length, expected_output[0][0])
        self.assertEqual(substrings, expected_output[0][1])

    def test_mixed_characters(self):
        input_string = "ABBCCDEFG"
        expected_output = [(5, ['CDEFG'])]
        length, substrings = LongestSubstringFinder.find_longest_substring(input_string)
        self.assertEqual(length, expected_output[0][0])
        self.assertEqual(substrings[0], expected_output[0][1][0])


if __name__ == '__main__':
    unittest.main()
