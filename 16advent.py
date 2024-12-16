"""16advent.py
Los elfos están trabajando arduamente para limpiar los caminos llenos de nieve mágica ❄️. Esta nieve tiene una propiedad especial: si dos montículos de nieve idénticos y adyacentes se encuentran, desaparecen automáticamente.

Tu tarea es escribir una función que ayude a los elfos a simular este proceso. El camino se representa por una cadena de texto y cada montículo de nieve un carácter.

Tienes que eliminar todos los montículos de nieve adyacentes que sean iguales hasta que no queden más movimientos posibles.

El resultado debe ser el camino final después de haber eliminado todos los montículos duplicados:

remove_snow('zxxzoz') # -> "oz"
    # 1. Eliminamos "xx", quedando "zzoz"
    # 2. Eliminamos "zz", quedando "oz"

remove_snow('abcdd') # -> "abc"
    # 1. Eliminamos "dd", quedando "abc"

remove_snow('zzz') # -> "z"
    # 1. Eliminamos "zz", quedando "z"

remove_snow('a') # -> "a"
    # No hay montículos repetidos
"""

import unittest


class TestExapleCases(unittest.TestCase):
    def test_return_type_is_str(self):
        for case, _ in test_cases:
            self.assertIsInstance(remove_snow(case), str)

    def test_return_value_match(self):
        for case, expected in test_cases:
            self.assertEqual(remove_snow(case), expected)


test_cases = [("zxxzoz", "oz"), ("abcdd", "abc"), ("zzz", "z"), ("a", "a")]


def remove_snow(s: str) -> str:
    finished_search = False
    while not finished_search:
        alphabet = sorted([(str(char)) * 2 for char in set(list(s))])
        for group in alphabet:
            positions = []
            start = s.find(group)
            if start > -1:
                positions.append(start)
            for start in positions:
                s = s.replace(s[start : start + 2], "")
        finished_search = bool(len(positions) == 0)
    return s


def test_single_case(idx):
    case, expected = test_cases[idx]
    res = remove_snow(case)
    print(f"{case:^10} | {expected:^9} | {res == expected:^6} | {idx:^9}")


if __name__ == "__main__":
    header = f"{'TRAIL':^{10}} | {'EXPECTED':^{9}} | {'match':^6} | test case"
    print(header)
    test_single_case(0)

    for idx, (case, expected) in enumerate(test_cases):
        res = remove_snow(case)
        print(f"{case:^10} | {expected:^9} | {res == expected:^6} | {idx:^9}")

    unittest.main(verbosity=2)
