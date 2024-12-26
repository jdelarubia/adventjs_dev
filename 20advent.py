"""20advent.py
Santa Claus 🎅 is checking the list of gifts he must deliver this Christmas. However, some gifts are missing, others are duplicated, and some have incorrect quantities. He needs your help to solve the problem.

You will receive two arrays:

- received: List with the gifts Santa currently has.
- expected: List with the gifts Santa should have.

Your task is to write a function that, given received and expected, returns an object with two properties:

- missing: An object where the keys are the names of the missing gifts and the values are the quantities that are missing.
- extra: An object where the keys are the names of the extra or duplicated gifts and the values are the quantities that are extra.

Keep in mind that:

- Gifts may be repeated in both lists.
- The gift lists are unordered.
- If there are no missing or extra gifts, the corresponding properties (missing or extra) should be empty objects.

fix_gift_list(['puzzle', 'car', 'doll', 'car'], ['car', 'puzzle', 'doll', 'ball'])
# Returns:
# {
#   missing: { ball: 1 },
#   extra: { car: 1 }
# }

fix_gift_list(
  ['book', 'train', 'kite', 'train'],
  ['train', 'book', 'kite', 'ball', 'kite']
)
# Returns:
# {
#   missing: { ball: 1, kite: 1 },
#   extra: { train: 1 }
# }

fix_gift_list(
  ['bear', 'bear', 'car'],
  ['bear', 'car', 'puzzle', 'bear', 'car', 'car']
)
# Returns:
# {
#   missing: { puzzle: 1, car: 2 },
#   extra: {}
# }

fix_gift_list(['bear', 'bear', 'car'], ['car', 'bear', 'bear'])
# Returns:
# {
#   missing: {},
#   extra: {}
# }
lee elemento en received
  comprueba si está en expected
    si está, lo elimina de expected
        comprueba si el valor en missing es el esperado (expected)
    si no lo está, lo añade a missing
"""

import unittest

test_cases = [
    (
        ["puzzle", "car"],
        ["puzzle", "car", "ball"],
        {"missing": {"ball": 1}, "extra": {}},
    ),
    (
        ["car", "puzzle", "car"],
        ["puzzle", "car", "doll"],
        {"missing": {"doll": 1}, "extra": {"car": 1}},
    ),
    (
        ["train", "book", "kite"],
        ["train", "kite", "book", "kite"],
        {"missing": {"kite": 1}, "extra": {}},
    ),
    (["bear", "car"], ["bear", "car", "car"], {"missing": {"car": 1}, "extra": {}}),
    ([], ["bear", "car", "car"], {"missing": {"car": 2, "bear": 1}, "extra": {}}),
    (
        ["puzzle", "puzzle", "car"],
        ["puzzle", "car"],
        {"missing": {}, "extra": {"puzzle": 1}},
    ),
    (
        ["car"],
        ["car", "puzzle", "ball"],
        {"missing": {"puzzle": 1, "ball": 1}, "extra": {}},
    ),
    (
        ["bear", "bear", "car"],
        ["bear", "car", "puzzle", "bear", "car", "car"],
        {"missing": {"puzzle": 1, "car": 2}, "extra": {}},
    ),
    (["bear", "bear", "car"], ["car", "bear", "bear"], {"missing": {}, "extra": {}}),
]


class TestExampleCases(unittest.TestCase):
    def test_return_type_is_str(self):
        for received, expected, _ in test_cases:
            self.assertIsInstance(fix_gift_list(received, expected), dict)

    def test_return_value_match(self):
        for received, expected, expected_result in test_cases:
            self.assertEqual(fix_gift_list(received, expected), expected_result)


def fix_gift_list(received: list[str], expected: list[str]) -> dict[str, int]:
    missing, extra = {}, {}
    received_dict = {gift: received.count(gift) for gift in received}
    expected_dict = {gift: expected.count(gift) for gift in expected}
    for gift, qty in received_dict.copy().items():
        if gift not in expected_dict.keys():
            missing[gift] = qty
        else:
            if qty == expected_dict[gift]:
                pass
            elif qty > expected_dict[gift]:
                extra[gift] = qty - expected_dict[gift]
            else:
                missing[gift] = expected_dict[gift] - qty
    for gift, qty in expected_dict.copy().items():
        if gift not in received_dict.keys():
            missing[gift] = qty
    return {"missing": missing, "extra": extra}


if __name__ == "__main__":
    header = f"{'RECEIVED':<28} | {'EXPECTED':<32} | {'EXP RES':<37} | {'RESULT':<37} | {'match':^8}"
    print(header)
    for case in test_cases:
        received, expected, expected_result = case
        res = fix_gift_list(received, expected)
        print()
        print(
            f"{str(received):<28} | {str(expected):<32} | {str(expected_result):<37} | {str(res):<37} | {res == expected_result:^8}"
        )

    unittest.main(verbosity=2)
