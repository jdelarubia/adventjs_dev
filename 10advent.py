"""10advent.py
The elf programmers are creating a small magical assembler to control the machines in Santa Claus's workshop.

To assist them, we will implement a simple interpreter that supports the following magical instructions:

    MOV x y: Copies the value x (which can be a number or the content of a register) into register y
    INC x: Increments the content of register x by 1
    DEC x: Decrements the content of register x by 1
    JMP x y: If the value in register x is 0, then jumps to the instruction at index y and continues executing the program from there.

Expected behavior:

    If an attempt is made to access, increment, or decrement a register that has not been initialized, the default value 0 will be used.
    The jump with JMP is absolute and goes to the exact index indicated by y.
    Upon completion, the program should return the content of register A. If A did not have a defined value, it returns undefined.

const instructions = [
  'MOV -1 C', // copies -1 to register 'C',
  'INC C', // increments the value of register 'C'
  'JMP C 1', // jumps to the instruction at index 1 if 'C' is 0
  'MOV C A', // copies register 'C' to register 'A',
  'INC A' // increments the value of register 'A'
]

compile(instructions) // -> 2

/**
 Step-by-step execution:
 0: MOV -1 C -> The register C receives the value -1
 1: INC C    -> The register C becomes 0
 2: JMP C 1  -> C is 0, jumps to the instruction at index 1
 1: INC C    -> The register C becomes 1
 2: JMP C 1  -> C is 1, the instruction is ignored
 3: MOV C A  -> Copies register C to A. Now A is 1
 4: INC A    -> The register A becomes 2
 */

Note: Registers that have not been previously initialized are initialized to 0."""

import unittest

instructions1 = [
    "MOV -1 C",  # copies -1 to register 'C',
    "INC C",  # increments the value of register 'C'
    "JMP C 1",  # jumps to the instruction at index 1 if 'C' is 0
    "MOV C A",  # copies register 'C' to register 'A',
    "INC A",  # increments the value of register 'A'
]
expected1 = 2
instructions2 = ["MOV 0 A", "INC A"]
expected2 = 1
instructions3 = [
    "INC A",
    "INC A",
    "DEC A",
    "MOV A B",
]
expected3 = 1
instructions4 = [
    "MOV 5 B",  # B = 5
    "DEC B",  # B = 4
    "MOV B A",  # A = 4 (B)
    "INC A",  # A = 5
]
expected4 = 5
instructions5 = [
    "INC C",  # C = 0 + 1 = 1
    "DEC B",  # B = 0 - 1 = -1
    "MOV C Y",  # Y = 1 (C)
    "INC Y",  # Y =2
]
expected5 = None
instructions6 = ["MOV 2 X", "DEC X", "DEC X", "JMP X 1", "MOV X A"]
expected6 = -2
instructions7 = ["MOV 3 C", "DEC C", "DEC C", "DEC C", "JMP C 3", "MOV C A"]
expected7 = -1
test_cases = [
    (instructions1, expected1),
    (instructions2, expected2),
    (instructions3, expected3),
    (instructions4, expected4),  #!FAILS
    (instructions5, expected5),  #!FAILS
    (instructions6, expected6),  #!FAILS
]


class ExampleTestCases(unittest.TestCase):
    def test_return_type_is_bool(self):
        for test_case in test_cases:
            case, _ = test_case
            try:
                self.assertIsInstance(compile(case), int)
            except AssertionError:
                self.assertIsNone(compile(case), None)

    def test_return_value_matches_expected(self):
        for test_case in test_cases:
            case, expected = test_case
            self.assertEqual(compile(case), expected)


def compile(instructions):
    registers = {}
    n_instructions = len(instructions)
    i = 0
    while i < n_instructions:
        command, *operands = instructions[i].split()
        dest = operands[-1]
        if command == "MOV":
            source = operands[0]
            try:
                value = int(source)
            except ValueError:
                value = registers.get(source, 0)
            registers[dest] = value
        elif command == "INC":
            registers[dest] = registers.get(dest, 0) + 1
        elif command == "DEC":
            registers[dest] = registers.get(dest, 0) - 1
        elif command == "JMP":
            source, value = operands
            if registers.get(source, 0) == 0:
                i = int(value)
                continue
        i += 1
    return registers.get("A", None)


if __name__ == "__main__":
    for case, expected in test_cases:
        res = compile(case)
        print(f"instructions: {case} | res: {res} | expected: {expected}")
        assert res == expected

    unittest.main(verbosity=2)
