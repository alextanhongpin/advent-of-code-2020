def parse_rules(rule):
  label, rules = rule.split(':')
  a, b = rules.strip().split(' or ')

  def split_range(rng):
    l, r = rng.split('-')
    return range(int(l), int(r)+1)

  return (label, [split_range(a), split_range(b)])

def ticket_error_rate(input):
  rules = []
  tickets = []

  sections = 0
  for line in input:
    line = line.strip()
    if line == '':
      continue

    if line.startswith('your ticket:') or line.startswith('nearby tickets:'):
      sections += 1
      continue

    if sections == 0:
      _, rule = parse_rules(line)
      rules.extend(rule)
    if sections == 2:
      tickets.extend(map(int, line.split(',')))

  valid_tickets = {}
  for rng in rules:
    for i in rng:
      valid_tickets[i] = True
  
  total = 0
  for ticket in tickets:
    if ticket not in valid_tickets:
      total += int(ticket)
  return total


def ticket_departure(input):
  rules = {}
  your_ticket = []
  tickets = []
  valid_tickets = {'all':{}}

  sections = 0
  for line in input:
    line = line.strip()
    if line == '':
      continue

    if line.startswith('your ticket:') or line.startswith('nearby tickets:'):
      sections += 1
      continue

    if sections == 0:
      label, rule = parse_rules(line)
      if label not in rule:
        rules[label] = []
      rules[label].extend(rule)

    if sections == 1:
      your_ticket = list(map(int, line.split(',')))
      tickets.append(your_ticket)

    if sections == 2:
      tickets.append(list(map(int, line.split(','))))

  orders = {}
  for i, _ in enumerate(tickets[0]):
    orders[i] = set(rules.keys())

  for label in rules:
    valid_tickets[label] = {}
    for rng in rules[label]:
      for i in rng:
        valid_tickets[label][i] = True
        valid_tickets['all'][i] = True

  for ticket in tickets:
    for i, nr in enumerate(ticket):
      if nr not in valid_tickets['all']:
        break
      for label in list(orders[i]):
        if nr not in valid_tickets[label]:
          orders[i].remove(label)

  output = {}
  while bool(orders):
    keys = orders.keys()
    for k in keys:
      if len(orders[k]) == 1:
        key = k
        break
    if key is not None:
      output[key] = list(orders[key])[0]
    for o in orders:
      if key != o:
        orders[o].remove(output[key])
    del(orders[key])

  total = None
  for key in output:
    if output[key].startswith('departure'):
      if total is None:
        total = your_ticket[key]
      else:
        total *= your_ticket[key]
  return total

def part_one():
  with open('input_16.txt') as f:
    print(ticket_error_rate(f)) # 19070


def part_two():
  with open('input_16.txt') as f:
    print(ticket_departure(f)) # 161926544831

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()