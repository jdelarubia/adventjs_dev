"""04advent.py
It's time to put up the Christmas tree at home! 🎄 But this year we want it to be special. We're going to create a function that receives the height of the tree (a positive integer between 1 and 100) and a special character to decorate it.

The function should return a string that represents the Christmas tree, constructed as follows:

    The tree is made up of triangles of special characters.
    The spaces on the sides of the tree are represented with underscores _.
    All trees have a trunk of two lines, represented by the # character.
    The tree should always have the same length on each side.
    You must ensure the tree has the correct shape using line breaks \n for each line.

Examples:

const tree = createXmasTree(5, '*')
console.log(tree)
/*
____*____
___***___
__*****__
_*******_
*********
____#____
____#____
*/

const tree2 = createXmasTree(3, '+')
console.log(tree2)
/*
__+__
_+++_
+++++
__#__
__#__
*/

const tree3 = createXmasTree(6, '@')
console.log(tree3)
/*
_____@_____ l0 c1
____@@@____ l1 c3
___@@@@@___ l2 c5
__@@@@@@@__ l3 c7
_@@@@@@@@@_ l4 c8
@@@@@@@@@@@ l5 c9
_____#_____
_____#_____
*/

Make sure to use line breaks \n at the end of each line, except for the last one.
"""

import unittest


def createXmasTree(height, ornament):
    assert 0 < height < 101
    tree = ""
    max_width = height * 2 - 1
    middle_point = max_width // 2
    branch_width = 1
    for _ in range(height):
        branch_str = ornament * branch_width
        blanks = (max_width - branch_width) // 2
        tree += ("_" * blanks) + branch_str + ("_" * blanks) + "\n"
        branch_width += 2
    trunk = f"{"_" * middle_point}#{"_" * middle_point}"
    return tree + "".join([trunk, "\n", trunk])


test_case1 = (5, "*")
test_case2 = (3, "+")
test_case3 = (6, "@")
test_cases = [test_case1, test_case2, test_case3]


class ExampleTestCases(unittest.TestCase):
    def test_return_type_is_str(self):
        expected = str
        for case in test_cases:
            height, ornament = case
            self.assertIsInstance(createXmasTree(height, ornament), expected)

    def test_last_branch_is_a_branch(self):
        expected = "#"
        for case in test_cases:
            height, ornament = case
            last_branch = createXmasTree(height, ornament).split("\n")[height + 1]
            self.assertIn(expected, last_branch)

    def test_last_character_is_not_cr(self):
        for case in test_cases:
            height, ornament = case
            tree = createXmasTree(height, ornament)
            self.assertIsNot(tree[-1], "\n")


if __name__ == "__main__":
    print(createXmasTree(5, "*"))
    print(createXmasTree(3, "+"))
    print(createXmasTree(6, "@"))
    unittest.main(verbosity=2)
