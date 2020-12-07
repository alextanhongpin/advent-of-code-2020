import re

def valid_passports(input):
  passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

  def build_passport(fields):
    kv = [field.split(':') for field in fields]
    return {k: v for k, v in kv if v}

  def validate_passport(passport):
    for field in passport_fields:
      if field not in passport:
        return False
    return True

  fields = []
  passports = []
  for line in input:
    line = line.strip()
    if line == '':
      passport = build_passport(fields)
      if validate_passport(passport):
        passports.append(passport)
      fields = []
    else:
      fields.extend(line.split(' '))

  return passports

def part_one():
  with open('2020/input_04.txt') as f:
    print(len(valid_passports(f)))

def part_two():
  def validate_birth_year(passport):
    return 1920 <= int(passport['byr']) <= 2002

  def validate_issue_year(passport):
    return 2010 <= int(passport['iyr']) <= 2020
  
  def validate_expiration_year(passport):
    return 2020 <= int(passport['eyr']) <= 2030
  
  def validate_height(passport):
    hgt = passport['hgt']
    if hgt.endswith('cm'):
      hgt = int(hgt.replace('cm', ''))
      return 150 <= hgt <= 193
    elif hgt.endswith('in'):
      hgt = int(hgt.replace('in', ''))
      return 59 <= hgt <= 76
    else:
      return False
  
  def validate_hair_color(passport):
    return re.match('^#[0-9a-f]{6}$', passport['hcl'])  is not None

  def validate_eye_color(passport):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for color in colors:
      if passport['ecl'] == color:
        return True
    return False

  def validate_passport_id(passport):
    return re.match('^[0-9]{9}$', passport['pid']) is not None
    
  with open('2020/input_04.txt') as f:
    passports = valid_passports(f)
    validations = [validate_birth_year, validate_issue_year, validate_expiration_year, validate_height, validate_hair_color, validate_eye_color, validate_passport_id]
    valid_counts = 0
    for passport in passports:
      valid = True
      for validation in validations:
        if not validation(passport):
          valid = False
          break
      if valid:
        valid_counts += 1
    print(valid_counts)

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()