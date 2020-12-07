from collections import Counter


def part_one():
  def valid_password(password, char, rng):
    min, max = rng
    return min <= Counter(password)[char] <= max

  valid = 0
  with open('2020/02_input.txt') as f:
    for line in f:
      rng, char, password = line.split(' ')
      char = char[:-1]
      min, max = rng.split('-')
      valid += valid_password(password, char, (int(min), int(max)))
  print(valid)

def part_two():
  def valid_password(password, char, position):
    first, last = position
    return (password[first] == char) != (password[last] == char)

  valid = 0
  with open('2020/02_input.txt') as f:
    for line in f:
      rng, char, password = line.split(' ')
      char = char[:-1]
      min, max = rng.split('-')
      valid += valid_password(password, char, (int(min)-1, int(max)-1))
  print(valid)

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()