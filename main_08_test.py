import unittest
from main_08 import boot, swap, build_instructions

input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split("\n")

class TestBoot(unittest.TestCase):
  def test_boot(self):
    n = boot(build_instructions(input))
    self.assertEqual(n, (5, True))

  def test_swap(self):
    n = swap(build_instructions(input))
    self.assertEqual(n, 8)

if __name__ == '__main__':
  unittest.main()