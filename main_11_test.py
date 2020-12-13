import unittest

from main_11 import build_seat, build_stable_seats, occupied_seats

input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split('\n')

class TestSeat(unittest.TestCase):
  def test_seat(self):
    self.assertEqual('\n'.join(build_seat(input)), """#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##""")

    self.assertEqual('\n'.join(build_stable_seats(input)), """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##""")
    self.assertEqual(occupied_seats(input), 37)

  def test_continuous(self):
    self.assertEqual(occupied_seats(input, True), 23)

if __name__ == '__main__':
  unittest.main()