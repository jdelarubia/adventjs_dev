"""09advent.py
The elves are playing with a magical train 🚂 that carries gifts. This train moves on a board represented by an array of strings.

The train consists of an engine (@), followed by its carriages (o), and must collect magical fruits (*) which serve as fuel. The movement of the train follows these rules:

You will receive two parameters board and mov.

board is an array of strings that represents the board:

    @ is the train's engine.
    o are the train's carriages.
    * is a magical fruit.
    · are empty spaces.

mov is a string that indicates the next movement of the train from the train's head @:

    'L': left
    'R': right
    'U': up
    'D': down.

With this information, you must return a string:

    'crash': If the train crashes into the edges of the board or itself.
    'eat': If the train collects a magical fruit (*).
    'none': If it moves without crashing or collecting any magical fruit.

Example:

board = ['·····', '*····', '@····', 'o····', 'o····']

print(moveTrain(board, 'U'))  # ➞ 'eat'
// Because the train moves up and finds a magical fruit

print(moveTrain(board, 'D'))  # ➞ 'crash'
// The train moves down and the head crashes into itself

print(moveTrain(board, 'L'))  # ➞ 'crash'
// The train moves to the left and crashes into the wall

print(moveTrain(board, 'R'))  # ➞ 'none'
// The train moves to the right and there is empty space on the right
"""

from typing import List, Literal

board2 = ["·····", "··*··", "··@··", "··o··", "··o··"]
moves2 = ["U"]
expected2 = "eat"
board3 = ["·····", "··*··", "··.··", "··o··", "··@··"]
moves3 = ["D"]
expected3 = "crash"
board4 = ["·····", "··*··", "··@··", "··o··", "··o··"]
moves4 = ["D"]
expected4 = "crash"
board5 = ["·····", "··*··", "··@··", "··o··", "··o··"]
moves5 = ["R"]
expected5 = "none"
board6 = ["··@··", "··o··", "·*o··", "··o··", "··o··"]
moves6 = ["U"]
expected6 = "crash"
board7 = ["··@··", "··o··", "·*o··", "··o··", "··o··"]
moves7 = ["L"]
expected7 = "none"
board8 = ["·····", "··@··", "··*··", "·····", "·····"]
moves8 = ["D"]
expected8 = "eat"

test_cases = [
    (board2, moves2, expected2),
    (board3, moves3, expected3),
    (board4, moves4, expected4),
    (board5, moves5, expected5),
    (board6, moves6, expected6),
    (board7, moves7, expected7),
    (board8, moves8, expected8),
]


def print_board(board):
    print()
    print("\n".join(board))


def move_train(
    board: List[str], mov: Literal["U", "D", "R", "L"]
) -> Literal["none", "crash", "eat"]:
    y_max = len(board) - 1
    x_max = len(board[0]) - 1
    # find head
    head = None
    for line_idx, line in enumerate(board):
        if "\u0040" in line:
            head = line.find("\u0040"), line_idx
            break
    if head:
        for move in mov:
            # find next position based on move
            x, y = head
            if move == "U":
                y -= 1
            elif move == "D":
                y += 1
            elif move == "L":
                x -= 1
            else:
                x += 1
            # check boundaries
            if x < 0 or x > x_max or y < 0 or y > y_max:
                return "crash"
            # grab new position board face
            next_face = board[y][x]
            # check if train crashed or eaten
            if next_face == "o":
                return "crash"
            elif next_face == "*":
                return "eat"
    return "none"


if __name__ == "__main__":
    i = 2
    for board, moves, expected in test_cases:
        print_board(board)
        res = move_train(board, moves)
        print(f"RESULT | EXPECTED | MOVES | test case {i}")
        print(f"{res:^6} | {expected:^10} | {moves}")
        i += 1
