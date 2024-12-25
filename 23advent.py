"""23advent.py
The elves are working on a system to verify children's gift lists 👧👦. However, some lists are incomplete and numbers are missing!

Your task is to write a function that, given an array of numbers, finds all the numbers that are missing between 1 and n (where n is the size of the array or the highest number in the array).

Keep in mind that:

- Numbers may appear more than once and others may be missing
- The array always contains positive integers
- Counting always starts from 1

find_missing_numbers([1, 2, 4, 6])  # [3, 5]

find_missing_numbers([4, 8, 7, 2])  # [1, 3, 5, 6]

find_missing_numbers([3, 2, 1, 1])  # []

find_missing_numbers([5, 5, 5, 3, 3, 2, 1])  # [4]
"""

import unittest

test_cases = [
    ([1, 2, 4, 6], [3, 5]),
    ([4, 8, 7, 2], [1, 3, 5, 6]),
    ([3, 2, 1, 1], []),
    ([5, 5, 5, 3, 3, 2, 1], [4]),
]


class ExampleTestCases(unittest.TestCase):
    def test_return_type_is_list(self):
        for case, _ in test_cases:
            self.assertIsInstance(find_missing_numbers(case), list)

    def test_return_value_matches_expected(self):
        for case, expected in test_cases:
            self.assertEqual(find_missing_numbers(case), expected)


def find_missing_numbers(nums):
    nums = list(sorted(set(nums)))
    upper_bound = len(nums)
    if max(nums) > len(nums):
        upper_bound = max(nums)
    return [n for n in range(1, upper_bound) if n not in nums]


if __name__ == "__main__":
    header = f"{'RESULT':>12} | {'EXPECTED':<12} | {'match':^6}"
    for case, expected in test_cases:
        res = find_missing_numbers(case)
        print(f"{str(res):>12} | {str(expected):<12} | {res == expected}")
        assert res == expected, f"{res = }, {expected = }"
