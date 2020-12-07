from collections import Counter


def parse_line(line):
    rng, char, password = line.split(' ')
    char = char[:-1]
    min, max = rng.split('-')
    return (password, char, int(min), int(max))

def part_one():
  def valid_password(password, char, min, max):
    return min <= Counter(password)[char] <= max

  valid = 0
  with open('input_02.txt') as f:
    for line in f:
      password, char, min, max = parse_line(line)
      valid += valid_password(password, char, min, max)
  print(valid)

def part_two():
  def valid_password(password, char, min, max):
    return (password[min-1] == char) != (password[max-1] == char)

  valid = 0
  with open('input_02.txt') as f:
    for line in f:
      password, char, min, max = parse_line(line)
      valid += valid_password(password, char, min, max)
  print(valid)

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()
