directions = ['top_left', 'top', 'top_right', 'left', 'right', 'bottom_left', 'bottom', 'bottom_right']
def check_seat(arr, position, direction, continuous=False):
  row, col = len(arr), len(arr[0])
  y, x = position
  dy, dx = 0, 0
  if direction.startswith('top'):
    dy = -1
  elif direction.startswith('bottom'):
    dy = +1
  if direction.endswith('left'):
    dx = -1
  elif direction.endswith('right'):
    dx = +1

  def traverse_seat():
    nonlocal y, x
    x = x + dx
    y = y + dy
    if y < 0 or x < 0 or x > col-1 or y > row-1:
      return None
    return (x, y)

  if continuous:
    while True:
      seat = traverse_seat()
      if seat is None:
        return seat
      x, y = seat
      if arr[y][x] != '.':
        return seat
  else:
    return traverse_seat()

def build_seat(input, continuous=False, cache=None):
  seats = [list(line.strip()) for line in input]
  row, col = len(seats), len(seats[0])
  output = [x[:] for x in [[''] * col] * row]
  for i in range(row):
    for j in range(col):
      if (i, j) in cache:
        adjacent_seats = cache[(i, j)]
      else:
        cache[(i, j)] = adjacent_seats = [seat for direction in directions 
                                          if (seat := check_seat(seats, (i, j), direction, continuous)) is not None]
      curr = seats[i][j]
      output[i][j] = curr
      if curr == 'L':
        if all([seats[y][x] != '#' for (x, y) in adjacent_seats]):
          output[i][j] = '#'
      elif curr == '#':
        max_seats = 5 if continuous else 4
        if sum([seats[y][x] == '#' for (x, y) in adjacent_seats]) >= max_seats:
          output[i][j] = 'L'
      else:
        output[i][j] = '.'
  return list(map(lambda row: ''.join(row), output))
      
def equal_list(a, b):
  for i, row in enumerate(a):
    if row != b[i]:
      return False
  return True

def build_stable_seats(input, continuous=False, cache=None):
  if cache is None:
    cache = {}
  result = build_seat(input, continuous, cache)
  i = 0
  while True:
    next_result = build_seat(result, continuous, cache)
    if equal_list(next_result, result): 
      break
    result = next_result
    i = i + 1
  return result

def occupied_seats(input, continuous=False):
  seats = build_stable_seats(input, continuous)
  occupied = 0
  for row in seats:
    occupied += row.count('#')
  return occupied

def part_one():
  with open('input_11.txt') as f:
    print(occupied_seats(f)) # 2247

def part_two():
  with open('input_11.txt') as f:
    print(occupied_seats(f, True)) # 2247

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()