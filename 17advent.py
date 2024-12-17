"""17advent.py
El Grinch ha estado haciendo de las suyas en el Polo Norte y ha sembrado bombas de carbón explosivo 💣 en la fábrica de juguetes de los duendes. Quiere que todos los juguetes queden inutilizados y por eso ha dejado una cuadrícula donde algunas celdas tienen carbón explosivo (true) y otras están vacías (false).

Los duendes necesitan tu ayuda para mapear las zonas peligrosas. Cada celda vacía debe mostrar un número que indique cuántas bombas de carbón explosivo hay en las posiciones adyacentes, incluidas las diagonales.

detect_bombs([
  [True, False, False],
  [False, True, False],
  [False, False, False]
])
# [
#   [1, 2, 1],
#   [2, 1, 1],
#   [1, 1, 1]
# ]

detect_bombs([
  [True, False],
  [False, False]
])
# [
#   [0, 1],
#   [1, 1]
# ]

detect_bombs([
  [True, True],
  [False, False],
  [True, True]
])

# [
#   [1, 1],
#   [4, 4],
#   [1, 1]
# ]

Nota: ¿Quieres una pista? Seguro que has jugado al juego de buscaminas antes… 😉
"""

test_cases = [
    # test 2
    (
        [[True, False, False], [False, True, False], [False, False, False]],
        [[1, 2, 1], [2, 1, 1], [1, 1, 1]],
    ),
    # test 3
    (
        [[False, True, False], [True, False, True], [False, True, False]],
        [[2, 2, 2], [2, 4, 2], [2, 2, 2]],
    ),
    # test 4
    ([[True, True], [True, True], [False, False]], [[3, 3], [3, 3], [2, 2]]),
    # test 5
    ([[True, True], [True, True]], [[3, 3], [3, 3]]),
    # test 6
    (
        [[False, False, False], [False, True, False], [False, False, False]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    ),
    # test 7
    (
        [[True, False], [False, False]],
        [[0, 1], [1, 1]],
    ),
    (
        # case:
        [[True, True], [False, False], [True, True]],
        # expected:
        [[1, 1], [4, 4], [1, 1]],
    ),
]


def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
    def check_coordinates(x: int, y: int) -> bool:
        rows = len(grid)
        columns = len(grid[0])
        if x < 0 or x > rows or y < 0 or y > columns:
            return False
        try:
            return grid[x][y] is True
        except IndexError:
            pass
        return False

    def check_surroundings(row: int, column: int):
        bombs = 0
        if check_coordinates(row, column - 1):
            bombs += 1
        if check_coordinates(row, column + 1):
            bombs += 1
        if check_coordinates(row + 1, column + 1):
            bombs += 1
        if check_coordinates(row + 1, column):
            bombs += 1
        if check_coordinates(row + 1, column - 1):
            bombs += 1
        if check_coordinates(row - 1, column - 1):
            bombs += 1
        if check_coordinates(row - 1, column):
            bombs += 1
        if check_coordinates(row - 1, column + 1):
            bombs += 1
        return bombs

    rows = len(grid)
    columns = len(grid[0])
    mines = [[0 for _ in range(columns)] for _ in range(rows)]
    row = 0
    while row < rows:
        column = 0
        while column < columns:
            bombs = check_surroundings(row, column)
            mines[row][column] = bombs
            column += 1
        row += 1
    return mines


def test_single_case(idx):
    test_case, expected = test_cases[idx]
    res = detect_bombs(test_case)
    print(f"{idx:^11} | {res==expected:^6}")


if __name__ == "__main__":
    header = f"test case # | {'match':^6}\n"
    print(header + len(header) * "-")

    for idx, (case, expected) in enumerate(test_cases):
        test_single_case(idx)
