"""15advent.py
ChatGPT has arrived at the North Pole and the elf Sam Elfman is working on an application for managing gifts and children.

To enhance the presentation, he wants to create a function draw_table that receives an array of objects and converts it into a text table.

The drawn table should represent the object data as follows:

    It has a header with the column name.
    The column name has the first letter capitalized.
    Each row should contain the values of the objects in the corresponding order.
    Each value must be left-aligned.
    Fields always leave a space on the left.
    Fields leave the necessary space on the right to align the box.

Look at the example to see how you should draw the table:

draw_table([
  { "name": 'Alice', "city": 'London' },
  { "name": 'Bob', "city": 'Paris' },
  { "name": 'Charlie', "city": 'New York' }
])
    # +---------+-----------+
    # | Name    | City      |
    # +---------+-----------+
    # | Alice   | London    |
    # | Bob     | Paris     |
    # | Charlie | New York  |
    # +---------+-----------+

draw_table([
  { "gift": 'Doll', "quantity": 10 },
  { "gift": 'Book', "quantity": 5 },
  { "gift": 'Music CD', "quantity": 1 }
])
    # +----------+----------+
    # | Gift     | Quantity |
    # +----------+----------+
    # | Doll     | 10       |
    # | Book     | 5        |
    # | Music CD | 1        |
    # +----------+----------+
"""

test_cases = [
    [{"name": "Alice", "city": "London"}],
    [
        {"name": "Alice", "city": "London"},
        {"name": "Bob", "city": "Paris"},
        {"name": "Charlie", "city": "New York"},
    ],
    [
        {"gift": "Doll", "quantity": 10},
        {"gift": "Book", "quantity": 5},
        {"gift": "Music CD", "quantity": 1},
    ],
    [{"id": 1, "score": 95}, {"id": 2, "score": 85}],
    [{"id": "midugato", "isCat": True}, {"id": "miduperro", "isCat": False}],
    [
        {"game": "indianajones", "subtitle": "the game"},
        {"game": "pokemonblue", "subtitle": ""},
    ],
]


def draw_table(data: list[dict[str, str | int]]) -> str:
    columns = [col_name for col_name in data[0].keys()]
    col1, col2 = columns
    col1 = col1[0].upper() + col1[1:]
    col2 = col2[0].upper() + col2[1:]
    width_col1 = len(col1)
    width_col2 = len(col2)
    for o in data:
        v1, v2 = o.values()
        if len(str(v1)) > width_col1:
            width_col1 = len(str(v1))
        if len(str(v2)) > width_col2:
            width_col2 = len(str(v2))
    head = "+" + "-" * (width_col1 + 2) + "+" + "-" * (width_col2 + 2) + "+"
    res = head + "\n"
    res += "".join(f"| {col1:{width_col1}} | {col2:{width_col2}} |") + "\n"
    res += head + "\n"
    for o in data:
        c1, c2 = o.values()
        res += "".join(f"| {c1:<{width_col1}} | {c2:<{width_col2}} |\n")
    return res + head


if __name__ == "__main__":
    for case in test_cases:
        print(draw_table(case))
