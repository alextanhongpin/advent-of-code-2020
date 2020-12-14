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
      binstr = bin(int(value)).zfill(len(mask)).replace('b', '0')

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


def part_one():
  with open('input_14.txt') as f:
    print(binary_mask(f)) # 6631883285184

def main():
  part_one()

if __name__ == '__main__':
  main()