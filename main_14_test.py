import unittest

from main_14 import binary_mask, binary_mask2

input1 = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split('\n')

input2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split('\n')

class TestBinaryMask(unittest.TestCase):
  def test_binary_mask(self):
    self.assertEqual(binary_mask(input1), 165)

  def test_binary_mask2(self):
    self.assertEqual(binary_mask2(input2), 208)

if __name__ == '__main__':
  unittest.main()