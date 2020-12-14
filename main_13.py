from collections import defaultdict 

def parse_input(input):
  input = [line.strip() for line in input]
  ts, bus_ids = int(input[0]), input[1]
  bus_ids = [int(bus_id) for bus_id in bus_ids.split(',') if bus_id != 'x']
  return ts, bus_ids

def schedule(input):
  ts, bus_ids = parse_input(input)
  result = []

  def check_earliest_ride(n, bus_id):
    while n % bus_id != 0:
      n += 1
    return n

  for bus_id in bus_ids:
    result.append(check_earliest_ride(ts, bus_id))

  earliest_bus = bus_ids[result.index(min(result))]
  return (min(result) - ts) * earliest_bus

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