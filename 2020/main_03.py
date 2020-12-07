def trajectory(input, left, down):
  i = 0
  trees = 0
  print()
  for j, line in enumerate(input):
    line = line.strip()
    # First line
    if j == 0:
      i += left
      i %= len(line) 
    else:
      if j % down == 0:
        trees += line[i] == '#'
        i += left
        i %= len(line) 
  return trees

def part_one():
  with open('2020/input_03.txt') as f:
    print(trajectory(f, 3, 1))

def part_two():
  with open('2020/input_03.txt') as f:
    input = [line.strip() for line in f]
    a = trajectory(input, 1, 1)
    b = trajectory(input, 3, 1)
    c = trajectory(input, 5, 1)
    d = trajectory(input, 7, 1)
    e = trajectory(input, 1, 2)
    print(a * b * c * d * e)


def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()