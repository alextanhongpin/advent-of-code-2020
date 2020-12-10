def adapt(input):
  cache = {int(line.strip()): True for line in input}

  def connect(i = 0):
    if i == max(cache):
      return (0, 1)

    if i+1 in cache:
      l, r = connect(i+1)
      return (1 + l, r)
    elif (i+3 in cache):
      l, r = connect(i + 3)
      return (l, r + 1)
  ones, threes = connect(0)
  return ones * threes

def combination(input):
  cache = {int(line.strip()): True for line in input}

  def connect(i):
    if i == max(cache):
      return i-3 in cache

    total = 0
    if i+1 in cache:
      total += connect(i + 1)
    if i+2 in cache:
      total += connect(i + 2)
    if i+3 in cache: 
      total += connect(i + 3)
    return total
    
  return connect(0)

def part_one():
  with open('input_10.txt') as f:
    print(adapt(f))

def part_two():
  # TODO: Not solved.
  with open('input_10.txt') as f:
    print(combination(f))

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()