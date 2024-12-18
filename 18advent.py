"""18advent.py
Santa Claus tiene una agenda mágica 📇 donde guarda las direcciones de los niños para entregar los regalos. El problema: la información de la agenda está mezclada y malformateada. Las líneas contienen un número de teléfono mágico, el nombre de un niño y su dirección, pero todo está rodeado de caracteres extraños.

Santa necesita tu ayuda para encontrar información específica de la agenda. Escribe una función que, dado el contenido de la agenda y un número de teléfono, devuelva el nombre del niño y su dirección.

Ten en cuenta que en la agenda:

- Los números de teléfono están formateados como +X-YYY-YYY-YYY (donde X es uno o dos dígitos, e Y es un dígito).
- El nombre de cada niño está siempre entre < y >

La idea es que escribas una funcióna que, pasándole el teléfono completo o una parte, devuelva el nombre y dirección del niño. Si no encuentra nada o hay más de un resultado, debes devolver null.

agenda = "+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"

find_in_agenda(agenda, '34-600-123-456')
# { name: "Juan Perez", address: "Calle Gran Via 12" }

find_in_agenda(agenda, '600-987')
# { name: "Maria Gomez", address: "Plaza Mayor 45 Madrid 28013" }

find_in_agenda(agenda, '111')
# null
# Explicación: No hay resultados

find_in_agenda(agenda, '1')
# null
# Explicación: Demasiados resultados
"""

import unittest

agenda = """+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"""
test_cases = [
    ("34-600-123-456", {"name": "Juan Perez", "address": "Calle Gran Via 12"}),
    ("600-987", {"name": "Maria Gomez", "address": "Plaza Mayor 45 Madrid 28013"}),
    ("111", None),
    ("1", None),
]


class TestExampleCases(unittest.TestCase):
    def test_return_type_is_object(self):
        for needle, _ in test_cases:
            try:
                self.assertIsInstance(find_in_agenda(agenda, needle), dict)
            except AssertionError:
                self.assertIsNone(find_in_agenda(agenda, needle))

    def test_return_value_match_expected(self):
        for needle, expected in test_cases:
            self.assertEqual(find_in_agenda(agenda, needle), expected)


def find_in_agenda(agenda: str, phone: str) -> dict | None:
    def clean_person(person: str):
        person += " "
        name_start = person.find("<")
        name_end = person.find(">")
        name = person[name_start + 1 : name_end].strip()
        person = person.replace(f"<{name}>", "")
        ph_start = person.find("+")
        ph_end = person.find(" ", ph_start)
        phone = person[ph_start:ph_end].strip()
        person = person.replace(f"{phone}", "")
        address = person.strip()
        return {phone: {"name": name, "address": address}}

    # clean agenda
    entries = agenda.split("\n")
    diction = {}
    for line in entries:
        diction.update(clean_person(line))
    # search
    n_results = 0
    found = None
    for key, person in diction.items():
        if phone in key:
            n_results += 1
            found = person
    if n_results == 1:
        return found
    return None


def test_single_case(idx):
    needle, expected = test_cases[idx]
    res = find_in_agenda(agenda, needle)
    print(f"{needle:^15} | {expected == res:^6} | {idx:^9} | {str(res):<10}")


if __name__ == "__main__":
    header = f"{'NEEDLE':^{15}} | {'match':^6} | {'test case':^9} | {'RESULT':<{10}}"
    print(header + "\n" + "-" * len(header))

    for idx, (needle, expected) in enumerate(test_cases):
        test_single_case(idx)

    unittest.main(verbosity=2)
