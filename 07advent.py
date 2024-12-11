"""07advent.py
The grinch 👹 has passed through Santa Claus's workshop! And what a mess he has made. He has changed the order of some packages, so shipments cannot be made.

Luckily, the elf Pheralb has detected the pattern the grinch followed to jumble them. He has written the rules that we must follow to reorder the packages. The instructions are as follows:

    You will receive a string containing letters and parentheses.
    Every time you find a pair of parentheses, you need to reverse the content within them.
    If there are nested parentheses, solve the innermost ones first.
    Return the resulting string with parentheses removed, but with the content correctly reversed.

He left us some examples:

fixPackages('a(cb)de')  # ➞ "abcde"
# We reverse "cb" inside the parentheses

fixPackages('a(bc(def)g)h')  # ➞ "agdefcbh"
# 1st we reverse "def" → "fed", then we reverse "bcfedg" → "gdefcb"

fixPackages('abc(def(gh)i)jk')  # ➞ "abcighfedjk"
# 1st we reverse "gh" → "hg", then "defhgi" → "ighfed"

fixPackages('a(b(c))e')  # ➞ "acbe"
# 1st we reverse "c" → "c", then "bc" → "cb"
"""

import unittest

package2 = "a(bc)de"
expected2 = "acbde"
package3 = "a(bc(def)g)h"
expected3 = "agdefcbh"
package4 = "abc(def(gh)i)jk"
expected4 = "abcighfedjk"
package5 = "a(b(c))e"
expected5 = "acbe"
package6 = "a(b(cd(efg)))h"
expected6 = "acdgfebh"
package7 = "(abc(def(ghi)))"
expected7 = "defihgcba"
package8 = "a(cb)de"
expected8 = "abcde"
test_cases = [
    (package2, expected2),
    (package3, expected3),
    (package4, expected4),
    (package5, expected5),
    (package6, expected6),
    (package7, expected7),
    (package8, expected8),
]


class ExampleTestCases(unittest.TestCase):
    def test_return_type_is_str(self):
        for case, _ in test_cases:
            self.assertIsInstance(fix_packages(case), str)

    def test_return_value_match_expected(self):
        for idx, case, expected in enumerate(test_cases):
            self.assertEqual(fix_packages(case), expected, msg=f"ERROR TEST {idx}")


def fix_packages(packages: str):
    first = packages.find("(")
    last = packages.rfind(")")
    if last <= first:
        return packages
    fix_packages(packages[first + 1 : last])
    reversed = packages[last - 1 : first : -1]
    return (
        packages.replace(packages[first + 1 : last], reversed)
        .replace("(", "")
        .replace(")", "")
    )


if __name__ == "__main__":
    for case, expected in test_cases:
        res = fix_packages(case)
        print(f"encrypted: {case} | res: {res} | expected: {expected}")
        assert res == expected

    unittest.main(verbosity=2)
