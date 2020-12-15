import unittest

from main_15 import recite


class TestRecite(unittest.TestCase):
  def test_recite(self):
    self.assertEqual(recite([0, 3, 6]), 436)
    self.assertEqual(recite([1, 3, 2]), 1)
    self.assertEqual(recite([2, 1, 3]), 10)
    self.assertEqual(recite([1, 2, 3]), 27)
    self.assertEqual(recite([2, 3, 1]), 78)
    self.assertEqual(recite([3, 2, 1]), 438)
    self.assertEqual(recite([3, 1, 2]), 1836)

if __name__ == '__main__':
  unittest.main()