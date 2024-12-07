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
]) # True

inBox([
  "####",
  "#* #",
  "#  #",
  "####"
]) # True

inBox([
  "#####",
  "#   #",
  "#  #*",
  "#####"
]) # False

inBox([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]) # False
"""

import unittest

test_case2 = ["###", "#*#", "###"]  # true
expected2 = True
test_case3 = ["#*#", "###", "###"]  # false
expected3 = False
test_case4 = ["###", "# #", "###"]
expected4 = False
test_case5 = ["####", "#* #", "#  #", "####"]  # true
expected5 = True
test_case6 = ["#####", "#   #", "#  #*", "#####"]  # false
expected6 = False
test_case7 = ["#####", "#   #", "#   #", "#   #", "#####"]  # false
expected7 = False
test_case8 = ["#####", "#   #", "#   #", "*#  #", "#####"]
expected8 = False
test_case9 = ["##*##", "#   #", "#   #", "#   #", "#####"]
expected9 = False
test_case10 = ["####", "#  #", "##*#"]
expected10 = False
test_case11 = ["###", "###", "#*#"]
expected11 = False
test_case12 = ["#####", "#   #", "#  #*", "####"]
expected12 = False

test_cases = [
    (test_case2, expected2),
    (test_case3, expected3),
    (test_case4, expected4),
    (test_case5, expected5),
    (test_case6, expected6),
    (test_case7, expected7),
    (test_case8, expected8),
    (test_case9, expected9),
    (test_case10, expected10),
    (test_case11, expected11),
    (test_case12, expected12),
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
    border = "\u0023"
    max_width = len(box[0])
    top = box[0] == border * max_width
    bottom = box[-1] == border * max_width
    boxed = False
    if top and bottom:
        for line in box[1:-1]:
            first = line.find(border)
            gift = line.find("*", first + 1)
            last = line.find(border, gift + 1)
            if first < gift < last:
                boxed = True
                break
    return boxed and top and bottom


if __name__ == "__main__":
    for idx, test_case in enumerate(test_cases):
        case, expected = test_case
        print(f"resultado test {idx:2}: {in_box(case)}")
    unittest.main(verbosity=2)
