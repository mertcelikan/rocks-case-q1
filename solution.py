#!/usr/bin/env python3


class LongestSubstringFinder:
    def __init__(self):
        pass

    @staticmethod
    def find_longest_substring(s):
        start = maxLength = 0
        usedChar = {}
        longest_substrings = []

        for i, char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            else:
                if i - start + 1 > maxLength:
                    maxLength = i - start + 1
                    longest_substrings = [s[start:i + 1]]
                elif i - start + 1 == maxLength:
                    longest_substrings.append(s[start:i + 1])

            usedChar[char] = i

        return maxLength, longest_substrings


if __name__ == "__main__":
    input_string = input("input: ")
    if not input_string:
        print("Input cannot be empty. Please enter a valid string.")
    else:
        length, substrings = LongestSubstringFinder.find_longest_substring(input_string)
        print(f"output: {substrings[0]} length: {length}")