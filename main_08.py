def build_instructions(input):
  instructions = []

  for line in input:
    line = line.strip()
    instruction, value = line.split(" ")
    value = int(value)
    instructions.append((instruction, value))

  return instructions

def boot(instructions):
  acc = 0
  visited = set()
  idx = 0
  while True:
    instruction = instructions[idx]
    (instruction, value) = instruction

    if idx in visited:
      return (acc, True)
    visited.add(idx)
    last_idx = idx == len(instructions) - 1

    if instruction == "jmp":
      idx += value
    elif instruction == "acc":
      idx += 1
      acc += value
    else:
      idx += 1

    if last_idx:
      break
  return (acc, False)

def swap(instructions):
  mapping = {'jmp': 'nop', 'nop': 'jmp'}
  for (idx, (instruction, value)) in enumerate(instructions):
    if instruction in mapping:
      cpy = instructions[:]
      cpy[idx] = (mapping[instruction], value)
      (acc, duplicate) = boot(cpy)
      if not duplicate:
        return acc
  
def part_one():
  with open('input_08.txt') as f:
    print(boot(build_instructions(f)))

def part_two():
  with open('input_08.txt') as f:
    print(swap(build_instructions(f)))

def main():
  part_one()
  part_two()


if __name__ == '__main__':
  main()