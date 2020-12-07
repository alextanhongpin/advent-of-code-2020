import unittest
from main_03 import trajectory 

INPUT = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split('\n')

class TestTrajectory(unittest.TestCase):
  def test_part_one(self):
    self.assertEqual(trajectory(INPUT, 3, 1), 7)

  def test_part_two(self):
    a = trajectory(INPUT, 1, 2)
    b = trajectory(INPUT, 3, 1)
    c = trajectory(INPUT, 5, 1)
    d = trajectory(INPUT, 7, 1)
    e = trajectory(INPUT, 1, 2)
    self.assertEqual(a, 2)
    self.assertEqual(b, 7)
    self.assertEqual(c, 3)
    self.assertEqual(d, 4)
    self.assertEqual(e, 2)
    self.assertEqual(a * b * c * d * e, 336)

if __name__ == '__main__':
  unittest.main()