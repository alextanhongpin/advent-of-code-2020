def adapt(input):
  xs = [int(line.strip()) for line in input]
  xs = sorted([0, *xs, max(xs)+3])

  n1, n3 = 0, 0
  for i in range(len(xs)-1):
    delta = xs[i+1] - xs[i]
    if delta == 1:
      n1 += 1
    elif delta == 3:
      n3 += 1
  return n1 * n3

def combination(input):
  xs = [int(line.strip()) for line in input]
  xs = sorted([0, *xs, max(xs)+3])

  cache = {}
  def dp(i):
    if i == len(xs)-1:
      return 1
    
    if i in cache:
      return cache[i]

    total = 0
    for j in range(i+1, len(xs)):
      if xs[j] - xs[i] <= 3:
        total += dp(j)
    cache[i] = total
    return total
    
  return dp(0)

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