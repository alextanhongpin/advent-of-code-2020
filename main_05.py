
def build_boarding_pass(input):
  def bin_space_partitioning(value, lower_half='F', upper_half='B', rng = None):
    if value == lower_half:
      return rng[0]
    elif value == upper_half:
      return rng[1]
    elif value.startswith(lower_half):
      mid = rng[0] + (rng[1] - rng[0]) // 2
      return bin_space_partitioning(value[1:], lower_half=lower_half, upper_half=upper_half, rng=(rng[0], mid))
    elif value.startswith(upper_half):
      mid = rng[0] + (rng[1] - rng[0]) // 2 + 1
      return bin_space_partitioning(value[1:], lower_half=lower_half, upper_half=upper_half, rng=(mid, rng[1]))
    else:
      return rng

  row = bin_space_partitioning(input[:-3], lower_half='F', upper_half='B', rng=(0, 127))
  column = bin_space_partitioning(input[-3:], lower_half='L', upper_half='R', rng=(0, 7))
  seat_id = row * 8 + column
  return (row, column, seat_id)

def find_seats():
  seats = []
  with open('input_05.txt') as f:
    for line in f:
      line = line.strip()
      boarding_pass = build_boarding_pass(line)
      seats.append(boarding_pass[-1])
  return seats

def part_one():
  print('max seat', max(find_seats()))

def part_two():
  seats = find_seats()
  seats_sorted = sorted(seats)
  checked = {}
  for seat in seats_sorted:
    if (seat-1) not in checked and bool(checked):
      print('your seat:', seat-1)
    checked[seat] = True

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()