from collections import Counter

def poll(input, condition):
  group = []
  count = 0
  for line in input:
    line = line.strip()
    if line == '':
      count += condition(group)
      group = []
    else:
      group.append(line)
  count += condition(group)
  return count

def anyone(group):
  return len(set(''.join(group)))

def everyone(group):
  counter = Counter(''.join(group))
  count = 0
  for key in counter:
    if counter[key] == len(group):
      count += 1
  return count


def part_one():
  with open('input_06.txt') as f:
    print(poll(f, anyone)) # 6748

def part_two():
  with open('input_06.txt') as f:
    print(poll(f, everyone)) # 6748

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()