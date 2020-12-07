import unittest

from main_04 import valid_passports

class TestPassport(unittest.TestCase):
  def test_passport_valid(self):
    input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in""".split('\n')
    passports = valid_passports(input)
    self.assertEqual(len(passports), 2, 'must have 2 valid passports')

if __name__ == '__main__':
  unittest.main()