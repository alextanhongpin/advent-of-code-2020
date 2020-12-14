from collections import defaultdict

def navigate(input):
  east, north = 0, 0
  direction = 0
  directions = ['E', 'S', 'W', 'N']
  for line in input:
    line = line.strip()
    if line == '':
      continue
    action, value = line[0], int(line[1:])
    if action == 'F':
      curr = directions[direction]
      if curr == 'E':
        east += value
      elif curr == 'W':
        east -= value
      elif curr == 'N':
        north += value
      else:
        north -= value
    elif action == 'R':
      direction = (direction+int(value//90))%len(directions)
    elif action == 'L':
      direction = (direction-int(value//90))%len(directions)
    elif action == 'N':
      north += value
    elif action == 'S':
      north -= value
    elif action == 'E':
      east += value
    elif action == 'W':
      east -= value
  return abs(east) + abs(north)
      

def navigate2(input):
  east, north = 10, 1
  ship_east, ship_north = 0, 0
  for line in input:
    line = line.strip()
    if line == '':
      continue
    action, value = line[0], int(line[1:])
    if action == 'F':
      ship_east += east * value
      ship_north += north * value
    elif action == 'R':
      rotation = value % 360
      if rotation == 90:
        east, north = north, -east
      if rotation == 180:
        east, north = -east, -north
      if rotation == 270:
        east, north = -north, east
    elif action == 'L':
      rotation = value % 360
      if rotation == 90:
        east, north = -north, east
      if rotation == 180:
        east, north = -east, -north
      if rotation == 270:
        east, north = north, -east
    elif action == 'N':
      north += value
    elif action == 'S':
      north -= value
    elif action == 'E':
      east += value
    elif action == 'W':
      east -= value
  return abs(ship_east) + abs(ship_north)

def part_one():
  with open('input_12.txt') as f:
    print(navigate(f)) # 757

def part_two():
  with open('input_12.txt') as f:
    print(navigate2(f)) # 51249

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()