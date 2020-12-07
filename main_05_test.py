import unittest

from main_05 import build_boarding_pass

class TestBoardingPass(unittest.TestCase):
  def test_boarding_pass(self):

    tests = [
      ('FBFBBFFRLR', (44, 5, 357)),
      ('FFFBBBFRRR', (14, 7, 119)),
      ('BBFFBBFRLL', (102, 4, 820))
    ]
    for test in tests:
      boarding_pass = build_boarding_pass(test[0])
      self.assertEqual(boarding_pass, test[-1])

if __name__ == '__main__':
  unittest.main()