"""06advent.py

We have already wrapped hundreds of presents 🎁… but an elf forgot to check if the present, represented by an asterisk *, is inside the box.

The box has a present (*) and counts as "inside the box" if:

    It is completely surrounded by # on the box's edges.
    The * is not on the box's edges.

Keep in mind that the * can be inside, outside, or may not even be there. We must return true if the * is inside the box and false otherwise.

DON'T USE IMPORTS

Examples:

inBox([
  "###",
  "#*#",
  "###"
]) // ➞ true

inBox([
  "####",
  "#* #",
  "#  #",
  "####"
]) // ➞ true

inBox([
  "#####",
  "#   #",
  "#  #*",
  "#####"
]) // ➞ false

inBox([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]) // ➞ false
"""

import unittest

test_case1 = ["###", "#*#", "###"]  # true
expected1 = True
test_case2 = ["####", "#* #", "#  #", "####"]  # true
expected2 = True
test_case3 = ["#####", "#   #", "#  #*", "#####"]  # false
expected3 = False
test_case4 = ["#####", "#   #", "#   #", "#   #", "#####"]  # false
expected4 = False
test_case6 = ["#####", "#   #", "#  #*", "####"]
expected6 = False

test_case8 = ["#####", "#   #", "#   #", "*#  #", "#####"]
expected8 = False
test_case9 = ["##*##", "#   #", "#   #", "#   #", "#####"]
expected9 = False
test_case10 = ["####", "#  #", "##*#"]
expected10 = False
test_case11 = ["###", "###", "#*#"]
expected11 = False
test_cases = [
    (test_case1, expected1),
    (test_case2, expected2),
    (test_case3, expected3),
    (test_case4, expected4),
    (test_case6, expected6),
    (test_case8, expected8),
    (test_case9, expected9),
    (test_case10, expected10),
    (test_case11, expected11),
]


class ExampleTestCases(unittest.TestCase):
    def test_return_type_is_bool(self):
        for test_case in test_cases:
            case, _ = test_case
            self.assertIsInstance(in_box(case), bool)

    def test_return_expected_value(self):
        for test_case in test_cases:
            case, expected = test_case
            self.assertIs(in_box(case), expected)


def in_box(box):
    max_width = len(box[0])
    top = box[0] == "#" * max_width
    bottom = box[-1] == "#" * max_width
    boxed = False
    if top and bottom:
        for line in box[1:-1]:
            first = line.find("#")
            gift = line.find("*", first + 1)
            last = line.find("#", gift + 1)
            if first < gift < last:
                boxed = True
                break
    return boxed and top and bottom


if __name__ == "__main__":
    for test_case in test_cases:
        case, expected = test_case
        print(in_box(case))
    unittest.main(verbosity=2)
