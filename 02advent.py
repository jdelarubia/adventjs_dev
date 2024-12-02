"""02advent.py
Santa Claus 🎅 wants to frame the names of the good children to decorate his workshop 🖼️, but the frame must follow specific rules. Your task is to help the elves generate this magical frame.

Rules:

    - Given an array of names, you must create a rectangular frame that contains all of them.
    - Each name must be on a line, aligned to the left.
    - The frame is built with * and has a border one line thick.
    - The width of the frame automatically adapts to the longest name plus a margin of 1 space on each side.

Example:
createFrame(['midu', 'madeval', 'educalvolpz'])

// Expected result:
***************
* midu        *
* madeval     *
* educalvolpz *
***************

createFrame(['midu'])

// Expected result:
********
* midu *
********

createFrame(['a', 'bb', 'ccc'])

// Expected result:
*******
* a   *
* bb  *
* ccc *
*******

createFrame(['a', 'bb', 'ccc', 'dddd'])
"""

import unittest


def createFrame(names):
    max_len = max([len(name) for name in names])
    return (
        "*" * (max_len + 4)
        + "\n"
        + "".join(f"* {name + ' ' * (max_len - len(name))} *\n" for name in names)
        + "*" * (max_len + 4)
    )


class ExampleTestCases(unittest.TestCase):
    test_case_1 = ["midu", "madeval", "educalvolpz"]
    test_case_2 = ["midu"]
    test_case_3 = ["a", "bb", "ccc"]
    test_case_4 = ["a", "bb", "ccc", "dddd"]
    test_cases = [test_case_1, test_case_2, test_case_3, test_case_4]

    def test_type_of_returned_string_is_str(self):
        expected = str
        for case in self.test_cases:
            self.assertIsInstance(createFrame(case), expected)

    def test_max_length_of_returned_string(self):
        for case in self.test_cases:
            expected = max([len(name) for name in case]) + 4  # adds 4 blanks + CR
            self.assertEqual(len(createFrame(case).split("\n")[0]), expected)


if __name__ == "__main__":
    print(createFrame(["midu"]))
    print(createFrame(["midu", "madeval", "educalvolpz"]))
    print(createFrame(["a", "bb", "ccc"]))
    print(createFrame(["a", "bb", "ccc", "dddd"]))
    unittest.main(verbosity=2)
