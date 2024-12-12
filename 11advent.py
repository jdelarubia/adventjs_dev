"""11advent.py
El Grinch ha hackeado 🏴‍☠️ los sistemas del taller de Santa Claus y ha codificado los nombres de todos los archivos importantes. Ahora los elfos no pueden encontrar los archivos originales y necesitan tu ayuda para descifrar los nombres.

Cada archivo sigue este formato:

- Comienza con un número (puede contener cualquier cantidad de dígitos).
- Luego tiene un guion bajo _.
- Continúa con un nombre de archivo y su extensión.
- Finaliza con una extensión extra al final (que no necesitamos).

Ten en cuenta que el nombre de los archivos pueden contener letras (a-z, A-Z), números (0-9), otros guiones bajos (_) y guiones (-).

Tu tarea es implementar una función que reciba un string con el nombre de un archivo codificado y devuelva solo la parte importante: el nombre del archivo y su extensión.
Ejemplos:

decode_filename('2023122512345678_sleighDesign.png.grinchwa')  # ➞ "sleighDesign.png"

decode_filename('42_chimney_dimensions.pdf.hack2023')  # ➞ "chimney_dimensions.pdf"

decode_filename('987654321_elf-roster.csv.tempfile')  # ➞ "elf-roster.csv"
"""

import unittest

test_cases = [
    ("2023122512345678_sleighDesign.png.grinchwa", "sleighDesign.png"),  # test2
    ("42_chimney_dimensions.pdf.hack2023", "chimney_dimensions.pdf"),  # test3
    ("987654321_elf-roster.csv.tempfile", "elf-roster.csv"),  # test4
    (
        "2024120912345678_magic_wand-blueprint.jpg.grinchbackup",
        "magic_wand-blueprint.jpg",
    ),  # test5
    ("51231_trainSchedule.txt.extra", "trainSchedule.txt"),  # test6
]


class ExampleTestCases(unittest.TestCase):
    def test_return_type_is_str(self):
        for case, expected in test_cases:
            self.assertIsInstance(decode_filename(case), str)

    def test_return_value_match_expected(self):
        for case, expected in test_cases:
            self.assertEqual(decode_filename(case), expected)


def decode_filename(filename: str) -> str:
    segments = filename.split("_")[1:]
    name = "_".join(segments)
    last = name.split(".")[:-1]
    name = ".".join(last)
    return name


def decode_filename_local(filename: str) -> str:
    """TypeError: ".".join is not a function"""
    # clean last extension
    segments = filename.split(".")
    filename = ".".join(segments[:-1])
    segments = filename.split("_")
    # clean first segment
    filename = "_".join(segments[1:])
    return filename


if __name__ == "__main__":
    for case, expected in test_cases:
        res = decode_filename(case)
        print(f"encrypted: {case} | res: {res} | expected: {expected}")
        assert res == expected

    unittest.main(verbosity=2)
