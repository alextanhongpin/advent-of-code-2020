import unittest

from main_09 import preamble

input = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split('\n')

class TestPreamble(unittest.TestCase):
  def test_preamble(self):
    self.assertEqual(preamble(input, 5), 127)

if __name__ == '__main__':
  unittest.main()