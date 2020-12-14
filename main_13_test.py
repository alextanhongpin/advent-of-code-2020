import unittest

from main_13 import schedule, schedule2

input = """939
7,13,x,x,59,x,31,19""".split('\n')

class TestSchedule(unittest.TestCase):
  def test_schedule(self):
    self.assertEqual(schedule(input), 295)

  def test_schedule2(self):
    self.assertEqual(schedule2(input), 1068781)

if __name__ == '__main__':
  unittest.main()