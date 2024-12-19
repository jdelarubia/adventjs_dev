"""07advent.py
The grinch 👹 has passed through Santa Claus's workshop! And what a mess he has made. He has changed the order of some packages, so shipments cannot be made.

Luckily, the elf Pheralb has detected the pattern the grinch followed to jumble them. He has written the rules that we must follow to reorder the packages. The instructions are as follows:

- You will receive a string containing letters and parentheses.
- Every time you find a pair of parentheses, you need to reverse the content within them.
- If there are nested parentheses, solve the innermost ones first.
- Return the resulting string with parentheses removed, but with the content correctly reversed.

He left us some examples:

fixPackages('a(cb)de')s
    # ➞ "abcde"
    # We reverse "cb" inside the parentheses

fixPackages('a(bc(def)g)h')
    # ➞ "agdefcbh"
    # 1st we reverse "def" → "fed", then we reverse "bcfedg" → "gdefcb"

fixPackages('abc(def(gh)i)jk')
    # ➞ "abcighfedjk"
    # 1st we reverse "gh" → "hg", then "defhgi" → "ighfed"

fixPackages('a(b(c))e')
    # ➞ "acbe"
    # 1st we reverse "c" → "c", then "bc" → "cb"
"""

import unittest

test_cases = [
    ("a(bc)de", "acbde"),
    ("a(bc(def)g)h", "agdefcbh"),
    ("abc(def(gh)i)jk", "abcighfedjk"),
    ("a(b(c))e", "acbe"),
    ("a(b(cd(efg)))h", "acdgfebh"),
    ("(abc(def(ghi)))", "defihgcba"),
    ("a(cb)de", "abcde"),
]


class ExampleTestCases(unittest.TestCase):
    def test_return_type_is_str(self):
        for case, _ in test_cases:
            self.assertIsInstance(fix_packages(case), str)

    def test_return_value_match_expected(self):
        for idx, (case, expected) in enumerate(test_cases):
            self.assertEqual(fix_packages(case), expected, msg=f"ERROR TEST {idx}")


def fix_packages(packages: str):
    start = 0
    while start > -1:
        start = packages.rfind("(")
        end = packages.find(")", start)
        needle = packages[start + 1 : end]
        reversed = packages[start + 1 : end][::-1]
        packages = packages.replace(f"({needle})", reversed)
    return packages


def test_single_case(idx: int):
    package, expected = test_cases[idx]
    result = fix_packages(package[:])
    print(f"{result:^15} | {expected:^15} | {result:^15} | {result == expected:^10} ")


if __name__ == "__main__":
    header = f"{'CASE':^15} | {'EXPECTED':^15} | {'RESULT':^15} | {'MATCH':^10} "
    print(header + "\n" + "-" * len(header))
    for idx, (case, expected) in enumerate(test_cases):
        test_single_case(idx)

    unittest.main(verbosity=2)
