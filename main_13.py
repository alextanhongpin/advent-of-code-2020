from collections import defaultdict 

def parse_input(input):
  input = [line.strip() for line in input]
  ts, bus_ids = int(input[0]), input[1]
  bus_ids = [int(bus_id) for bus_id in bus_ids.split(',') if bus_id != 'x']
  return ts, bus_ids

def schedule(input):
  ts, bus_ids = parse_input(input)
  min_time, first_bus = float('inf'), None

  for bus_id in bus_ids:
    n = ts
    if n % bus_id != 0:
      n = (n // bus_id + 1) * bus_id
    if n < min_time:
      min_time = n
      first_bus = bus_id

  return (min_time - ts) * first_bus

def schedule2(input):
  input = [line.strip() for line in input]
  bus_ids = input[1].split(',')
  bus_ids = [(idx, int(bus_id)) for idx, bus_id in enumerate(bus_ids) if bus_id != 'x']

  t, step = bus_ids[0][0], bus_ids[0][1]
  for delta, bus_id in bus_ids[1:]:
    while ((t + delta) % bus_id) != 0:
      t += step
    step *= bus_id
  return t



def part_one():
  with open('input_13.txt') as f:
    print(schedule(f)) # 171

def part_two():
  with open('input_13.txt') as f:
    print(schedule2(f)) # 539746751134958

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()