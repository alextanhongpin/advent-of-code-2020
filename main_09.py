
def preamble(input, prev=5):
  def find_sum_pair(arr, target):
    cache = {}
    for n in arr:
      if target-n in cache:
        return target-n
      cache[n] = True
    return None
  last_n = [0] * prev
  for idx, line in enumerate(input):
    line = line.strip()
    n = int(line)
    if idx > prev:
      if find_sum_pair(last_n, n) is None:
        return n
    last_n[idx % prev] = n

def part_one():
  with open('input_09.txt') as f:
    print(preamble(f, 25))

def part_two():
  with open('input_09.txt') as f:
    target = preamble(f, 25)
  
  prev_n = []
  with open('input_09.txt') as f:
    for line in f:
      line = line.strip()
      n = int(line)
      if n == target:
        break
      prev_n.append(n)
  i, j = 0, 2
  while True:
    rng = prev_n[i:j]
    n = sum(rng)
    if n == target:
      print(min(rng) + max(rng))
      break
    elif n > target:
      i += 1
    elif n < target:
      j += 1

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()