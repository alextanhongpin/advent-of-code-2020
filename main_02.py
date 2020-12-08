from collections import Counter


def parse_line(line):
    rng, char, password = line.split(' ')
    char = char[:-1]
    min, max = rng.split('-')
    return (password, char, int(min), int(max))

def part_one():
  def valid_password(password, char, min, max):
    return min <= Counter(password)[char] <= max

  with open('input_02.txt') as f:
    count = sum([valid_password(*parse_line(line)) for line in f])
    print(count) # 465

def part_two():
  def valid_password(password, char, min, max):
    return (password[min-1] == char) != (password[max-1] == char)

  with open('input_02.txt') as f:
    count = sum([valid_password(*parse_line(line)) for line in f])
    print(count) # 294

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()
