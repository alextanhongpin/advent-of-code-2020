import re


PATTERN = r'mem\[(\d+)\] = (\d+)'

def binary_mask(input):
  cache = {}

  lines = [line.strip() for line in input]
  for line in lines:
    if line.startswith('mask'):
      mask = line.split(' = ')[1]
    else:
      position, value = re.findall(PATTERN, line)[0]
      binstr = bin(int(value))[2:].zfill(len(mask))

      binval = ''
      for i in range(len(mask)):
        if mask[i] == '1':
          binval += mask[i]
        elif mask[i] == '0':
          binval += mask[i]
        else: 
          binval += binstr[i]
      cache[position] = int(binval, 2)

  return sum(cache.values())

def binary_mask2(input):
  cache = {}

  lines = [line.strip() for line in input]
  for line in lines:
    if line.startswith('mask'):
      mask = line.strip().split(' = ')[1]
    else:
      position, value = re.findall(PATTERN, line)[0]
      binstr = bin(int(position))[2:].zfill(len(mask))

      binval = ''
      for i in range(len(mask)):
        if mask[i] == '1':
          binval += '1'
        elif mask[i] == '0':
          binval += binstr[i]
        else: 
          binval += 'X'

      combinations = binval.count('X')
      for i in range(2**combinations):
        combination = bin(i)[2:].zfill(combinations)
        replaced = 0
        cpy = list(binval)
        for i, c in enumerate(cpy):
          if c == 'X':
            cpy[i] = combination[replaced]
            replaced += 1
        addr = int(''.join(cpy), 2)
        cache[addr] = int(value)

  return sum(cache.values())

def part_one():
  with open('input_14.txt') as f:
    print(binary_mask(f)) # 6631883285184


def part_two():
  with open('input_14.txt') as f:
    print(binary_mask2(f)) # 3161838538691

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()