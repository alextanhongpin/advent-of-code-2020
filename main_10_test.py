import unittest

from main_10 import adapt, combination

input1 = """16
10
15
5
1
11
7
19
6
12
4""".split('\n')

input2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".split('\n')

class TestPreamble(unittest.TestCase):
  def test_preamble(self):
    self.assertEqual(adapt(input1), 35)
    self.assertEqual(adapt(input2), 220)

  def test_combination(self):
    self.assertEqual(combination(input1), 8)
    self.assertEqual(combination(input2), 19208)

if __name__ == '__main__':
  unittest.main()