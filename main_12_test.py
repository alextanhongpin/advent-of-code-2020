import unittest

from main_12 import navigate, navigate2

input = """F10
N3
F7
R90
F11""".split('\n')

class TestNavigate(unittest.TestCase):
  def test_navigate(self):
    self.assertEqual(navigate(input), 25)
  def test_navigate2(self):
    self.assertEqual(navigate2(input), 286)

if __name__ == '__main__':
  unittest.main()