import unittest

from main_14 import binary_mask

input = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split('\n')

class TestBinaryMask(unittest.TestCase):
  def test_binary_mask(self):
    self.assertEqual(binary_mask(input), 165)

if __name__ == '__main__':
  unittest.main()