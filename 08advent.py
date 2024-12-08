"""08advent.py
It's time to select the fastest reindeer for Santa's journeys! 🦌🎄
Santa Claus has organized exciting reindeer races to determine which ones are in the best shape.

Your task is to display each reindeer's progress on a snow track in isometric format.

The information you receive:

    indices: An array of integers representing each reindeer's progress on the track:
    0: The lane is empty.
    Positive number: The reindeer's current position from the beginning of the track.
    Negative number: The reindeer's current position from the end of the track.
    length: The length of each lane.

Return a string representing the race track:

    Each lane has exactly length positions filled with snow (~).
    Each reindeer is represented with the letter r.
    Lanes are numbered at the end with /1, /2, etc.
    The view is isometric, so the lower lanes are shifted to the right.

Examples:

drawRace([0, 5, -3], 10)
/*
  ~~~~~~~~~~ /1
 ~~~~~r~~~~ /2
~~~~~~~r~~ /3
*/
~~~~~~~~~~
~~~~~r~~~~
~~~~~~~r~~

drawRace([2, -1, 0, 5], 8)
/*
   ~~r~~~~~ /1
  ~~~~~~~r /2
 ~~~~~~~~ /3
~~~~~r~~ /4
*/

drawRace([3, 7, -2], 12)
/*
  ~~~r~~~~~~~~ /1
 ~~~~~~~~r~~~ /2
~~~~~~~~~r~~ /3
*/
"""

import unittest

test_case2 = {"indices": [0, 5, -3], "length": 10}
expected2 = """  ~~~~~~~~~~ /1
 ~~~~~r~~~~ /2
~~~~~~~r~~ /3"""
test_case3 = {"indices": [2, -1, 0, 5], "length": 8}
expected3 = """   ~~r~~~~~ /1
  ~~~~~~~r /2
 ~~~~~~~~ /3
~~~~~r~~ /4"""
test_case4 = {"indices": [3, 7, -2], "length": 12}
expected4 = """  ~~~r~~~~~~~~ /1
 ~~~~~~~r~~~~ /2
~~~~~~~~~~r~ /3"""
test_case5 = {"indices": [0, 0, 0], "length": 6}
expected5 = """  ~~~~~~ /1
 ~~~~~~ /2
~~~~~~ /3"""
test_case6 = {"indices": [5, 3, -4], "length": 9}
expected6 = """  ~~~~~r~~~ /1
 ~~~r~~~~~ /2
~~~~~r~~~ /3"""
test_case7 = {"indices": [-1], "length": 8}
expected7 = "~~~~~~~r /1"
test_cases = [
    (test_case2, expected2),
    (test_case3, expected3),
    (test_case4, expected4),
    (test_case5, expected5),
    (test_case6, expected6),
    (test_case7, expected7),
]


class ExampleTestCases(unittest.TestCase):
    def test_return_type_is_bool(self):
        for case, _ in test_cases:
            indices, length = case.values()
            self.assertIsInstance(draw_race(indices, length), str)

    def test_return_expected_value(self):
        i = 0
        for case, expected in test_cases:
            indices, length = case.values()
            self.assertEqual(
                draw_race(indices, length), expected, msg=f"testing case {i}"
            )
            i += 1


def draw_race(indices, length):
    """optimized version"""
    n_tracks = len(indices)
    race_track = []
    for idx, reindeer in enumerate(indices):
        track = "~" * length
        track_pos = reindeer
        if reindeer < 0:
            track_pos = reindeer + length
        if reindeer != 0:
            track = track[:track_pos] + "r" + track[track_pos + 1 :]
        track = " " * (n_tracks - idx - 1) + track + f" /{idx+1}"

        race_track.append("".join(track))
    return "\n".join(race_track)


if __name__ == "__main__":
    i = 1
    for case, _ in test_cases:
        indices, length = case.values()
        print(f"test case {i}")
        print(draw_race(indices, length))
        i += 1

    unittest.main(verbosity=2)
