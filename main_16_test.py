import unittest

from main_16 import ticket_error_rate

input = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".split('\n')

class TestTicket(unittest.TestCase):
  def test_ticket_error_rate(self):
    self.assertEqual(ticket_error_rate(input), 71)

if __name__ == '__main__':
  unittest.main()