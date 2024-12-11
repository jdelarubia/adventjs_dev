"""07advent.py
The grinch 👹 has passed through Santa Claus's workshop! And what a mess he has made. He has changed the order of some packages, so shipments cannot be made.

Luckily, the elf Pheralb has detected the pattern the grinch followed to jumble them. He has written the rules that we must follow to reorder the packages. The instructions are as follows:

    You will receive a string containing letters and parentheses.
    Every time you find a pair of parentheses, you need to reverse the content within them.
    If there are nested parentheses, solve the innermost ones first.
    Return the resulting string with parentheses removed, but with the content correctly reversed.

He left us some examples:

fixPackages('a(cb)de')
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


def fix_packages(packages: str):
    print(packages)
    first = packages.find("(")
    last = packages.rfind(")")
    if last > first:
        return
    print(f"f: {first} : {packages[first]} | l: {last} : {packages[last]}")
    reversed = packages[last - 1 : first : -1]
    packages = packages.replace(packages[first:last], reversed)
    return fix_packages(packages)


def fix_packages_test(packages):
    first = packages.find("(")
    last = packages.rfind(")")
    reversed = ""
    if first < last:
        reversed = packages[last - 1 : first : -1]  #
        # print(reversed)
        packages = packages.replace(packages[first : last + 1], reversed)  #
        print(packages)
        return fix_packages(packages[first + 1 : last - 1])
    return packages


test_case1 = "a(cb)de"
expected1 = "abcde"

if __name__ == "__main__":
    print(fix_packages(test_case1))
