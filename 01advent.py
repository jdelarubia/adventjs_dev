"""01advent.py
Santa Claus 🎅 ha recibido una lista de números mágicos que representan regalos 🎁, pero algunos de ellos están duplicados y deben ser eliminados para evitar confusiones. Además, los regalos deben ser ordenados en orden ascendente antes de entregárselos a los elfos.

Tu tarea es escribir una función que reciba una lista de números enteros (que pueden incluir duplicados) y devuelva una nueva lista sin duplicados, ordenada en orden ascendente.

const gifts1 = [3, 1, 2, 3, 4, 2, 5]
const preparedGifts1 = prepareGifts(gifts1)
console.log(preparedGifts1) // [1, 2, 3, 4, 5]

const gifts2 = [6, 5, 5, 5, 5]
const preparedGifts2 = prepareGifts(gifts2)
console.log(preparedGifts2) // [5, 6]

const gifts3 = []
const preparedGifts3 = prepareGifts(gifts3)
console.log(preparedGifts3) // []
// No hay regalos, la lista queda vacía
"""

import unittest


def prepare_gifts(gifts):
    return sorted(set(gifts))


def test_one():
    gifts1 = [3, 1, 2, 3, 4, 2, 5]
    preparedGifts1 = prepare_gifts(gifts1)
    print(preparedGifts1)  # expected = [1, 2, 3, 4, 5]


def test_two():
    gifts2 = [6, 5, 5, 5, 5]
    preparedGifts2 = prepare_gifts(gifts2)
    print(preparedGifts2)  # expected = [5, 6]


def test_three():
    gifts3 = []
    preparedGifts3 = prepare_gifts(gifts3)
    print(preparedGifts3)  # expected = []


class ExampleTestCases(unittest.TestCase):
    test_case_1 = [3, 1, 2, 3, 4, 2, 5], [1, 2, 3, 4, 5]
    test_case_2 = [6, 5, 5, 5, 5], [5, 6]
    test_case_3 = [], []
    test_cases = [test_case_1, test_case_2, test_case_3]

    def test_returned_type_is_list(self):
        for case, expected in self.test_cases:
            self.assertIsInstance(prepare_gifts(case), list)

    def test_returned_values_match_expected(self):
        for case, expected in self.test_cases:
            self.assertEqual(prepare_gifts(case), expected)


if __name__ == "__main__":
    test_one()
    test_two()
    test_three()
    unittest.main(verbosity=2)
