"""05advent.py
Los elfos 🧝🧝‍♂️ de Santa Claus han encontrado un montón de botas mágicas desordenadas en el taller. Cada bota se describe por dos valores:

- type indica si es una bota izquierda (I) o derecha (R).
- size indica el tamaño de la bota.

Tu tarea es ayudar a los elfos a emparejar todas las botas del mismo tamaño que tengan izquierda y derecha. Para ello, debes devolver una lista con los tamaños disponibles después de emparejar las botas.

const shoes = [
  { type: 'I', size: 38 },
  { type: 'R', size: 38 },
  { type: 'R', size: 42 },
  { type: 'I', size: 41 },
  { type: 'I', size: 42 }
]
organizeShoes(shoes)  # [38, 42]

const shoes2 = [
  { type: 'I', size: 38 },
  { type: 'R', size: 38 },
  { type: 'I', size: 38 },
  { type: 'I', size: 38 },
  { type: 'R', size: 38 }
]
organizeShoes(shoes2)  # [38, 38]

const shoes3 = [
  { type: 'I', size: 38 },
  { type: 'R', size: 36 },
  { type: 'R', size: 42 },
  { type: 'I', size: 41 },
  { type: 'I', size: 43 }
]
organizeShoes(shoes3)  # []
"""

import unittest


def organizeShoes3(shoes):
    Derecha = []
    Izquierda = []
    for shoe in shoes:
        type, size = shoe.values()
        if type == "R":
            Derecha.append(size)
        else:
            Izquierda.append(size)
    Derecha.sort()
    Izquierda.sort()
    res = []
    for type in Derecha:
        try:
            Izquierda.remove(type)
        except ValueError:
            continue
        res.append(type)
    return res


def organizeShoes2(shoes):
    types = {"R": [], "I": []}
    for shoe in shoes:
        type, size = shoe.values()
        types[type].append(size)
    types["R"].sort()
    types["I"].sort()
    print(types)
    res = []
    for type in types["R"]:
        try:
            t = types["I"].remove(type)
            res.append(type)
        except ValueError:
            continue
    return res


def organizeShoes(shoes):
    res = []
    R = []
    I = []
    for shoe in shoes:
        type, size = shoe.values()
        if type == "R":
            if size in I:
                I.remove(size)
                res.append(size)
            else:
                R.append(size)
        else:  # type == "I"
            if size in R:
                R.remove(size)
                res.append(size)
            else:
                I.append(size)

    return list(res)


test_case1 = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
    {"type": "R", "size": 42},
    {"type": "I", "size": 41},
    {"type": "I", "size": 42},
]
expected1 = [38, 42]
test_case2 = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
    {"type": "I", "size": 38},
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
]
expected2 = [38, 38]
test_case3 = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 36},
    {"type": "R", "size": 42},
    {"type": "I", "size": 41},
    {"type": "I", "size": 43},
]
expected3 = []
test_cases = [(test_case1, expected1), (test_case2, expected2), (test_case3, expected3)]


class ExampleTestCases(unittest.TestCase):
    def test_return_type_is_list(self):
        expected = list
        for test_case in test_cases:
            case, _ = test_case
            self.assertIsInstance(organizeShoes(case), expected)

    def test_expected_values(self):
        for case, expected in test_cases:
            self.assertEqual(organizeShoes(case), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print(organizeShoes(test_case1))  # [38, 42]
    print(organizeShoes(test_case2))  # [38, 38]
    print(organizeShoes(test_case3))  # []
