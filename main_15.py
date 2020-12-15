def recite(input, target=2020):
  turns = {}
  for i, n in enumerate(input):
    turns[n] = [i+1]
    last = n
  
  for i in range(len(input), target):
    if last in turns and len(turns[last]) > 1:
      last = turns[last][-1] - turns[last][-2]
    else:
      last = 0
    if last not in turns:
      turns[last] = []
    turns[last].append(i+1)
    turns[last] = turns[last][-2:]
  return last


def part_one():
  print(recite([16,1,0,18,12,14,19]))


def part_two(): 
  # Super slow.
  print(recite([16,1,0,18,12,14,19], 30000000))

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()