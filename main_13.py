
def schedule(input):
  input = [line.strip() for line in input]
  ts, bus_ids = int(input[0]), input[1]
  bus_ids = [int(bus_id) for bus_id in bus_ids.split(',') if bus_id != 'x']
  result = []

  def check_earliest_ride(n, bus_id):
    while n % bus_id != 0:
      n += 1
    return n

  for bus_id in bus_ids:
    result.append(check_earliest_ride(ts, bus_id))

  earliest_bus = bus_ids[result.index(min(result))]
  return (min(result) - ts) * earliest_bus

def part_one():
  with open('input_13.txt') as f:
    print(schedule(f))

def main():
  part_one()

if __name__ == '__main__':
  main()