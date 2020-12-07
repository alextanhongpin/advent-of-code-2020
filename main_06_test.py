import unittest
from main_06 import poll, everyone, anyone

class TestPool(unittest.TestCase):
  def test_anyone_pool(self):
    input = """abc

a
b
c

ab
ac

a
a
a
a

b""".split('\n')
    count = poll(input, anyone)
    self.assertEqual(count, 11)
  
  def test_everyone_poll(self):
    input = """abc

a
b
c

ab
ac

a
a
a
a

b""".split('\n')
    count = poll(input, everyone)
    self.assertEqual(count, 6)




if __name__ == '__main__':
  unittest.main()