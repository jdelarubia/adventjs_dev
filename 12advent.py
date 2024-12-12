"""12advent.py
Estás en un mercado muy especial en el que se venden árboles de Navidad 🎄. Cada uno viene decorado con una serie de adornos muy peculiares, y el precio del árbol se determina en función de los adornos que tiene.

- *: Copo de nieve - Valor: 1
- o: Bola de Navidad - Valor: 5
- ^: Arbolito decorativo - Valor: 10
- #: Guirnalda brillante - Valor: 50
- @: Estrella polar - Valor: 100

Normalmente se sumarían todos los valores de los adornos y ya está…

Pero, ¡ojo! Si un adorno se encuentra inmediatamente a la izquierda de otro de mayor valor, en lugar de sumar, se resta su valor.

calculate_price('***')  # 3   (1 + 1 + 1)
calculate_price('*o')   # 4   (5 - 1)
calculate_price('o*')   # 6   (5 + 1)
calculate_price('*o*')  # 5  (-1 + 5 + 1)
calculate_price('**o*') # 6  (1 - 1 + 5 + 1)
calculate_price('o***') # 8   (5 + 3)
calculate_price('*o@')  # 94  (-5 - 1 + 100)
calculate_price('*#')   # 49  (-1 + 50)
calculate_price('@@@')  # 300 (100 + 100 + 100)
calculate_price('#@')   # 50  (-50 + 100)
calculate_price('#@Z')  # undefined (Z es desconocido)
"""

import unittest

test_cases = [
    ("***", 3),
    ("*o", 4),
    ("o*", 6),
    ("*o*", 5),
    ("**o*", 6),
    ("o***", 8),
    ("*o@", 94),
    ("*#", 49),
    ("@@@", 300),
    ("#@", 50),
    ("#@Z", None),  #! undefined
    ("^#", 40),
]


class TestExampleCases(unittest.TestCase):
    def test_return_type_is_int(self):
        for case, expected in test_cases:
            try:
                self.assertIsInstance(calculate_price(case), int)
            except AssertionError:
                self.assertIsNone(calculate_price(case))

    def test_returned_value_matches_expected(self):
        for case, expected in test_cases:
            self.assertEqual(calculate_price(case), expected)


def calculate_price(ornaments: str) -> int:
    prices = {"*": 1, "o": 5, "^": 10, "#": 50, "@": 100}
    total_value = 0
    for idx, current_ornament in enumerate(ornaments):
        if current_ornament not in prices.keys():
            return None  #! undefined
        current_value = prices[current_ornament]
        if idx > 0:
            prev_ornament = ornaments[idx - 1]
            prev_value = prices[prev_ornament]
            if prev_value < current_value:
                total_value -= prev_value * 2
        total_value += current_value
    return total_value


def calculate_price_while(ornaments: str) -> int:
    prices = {"*": 1, "o": 5, "^": 10, "#": 50, "@": 100}
    total_value = 0
    i = 0
    while i < len(ornaments):
        current_ornament = ornaments[i]
        if current_ornament not in prices.keys():
            return None  #! undefined
        current_value = prices.get(current_ornament, 0)
        if i > 0:
            prev_ornament = ornaments[i - 1]
            prev_value = prices.get(prev_ornament, 0)
            if prev_value < current_value:
                total_value -= prev_value * 2
        total_value += current_value
        i += 1
    return total_value


if __name__ == "__main__":
    print("RESULT | EXPECTED | ORNAMENTS")
    for case, expected in test_cases:
        res = calculate_price(case)
        print(f"{str(res):>6} | {str(expected):>8} | {case:^9}")

    unittest.main(verbosity=2)
