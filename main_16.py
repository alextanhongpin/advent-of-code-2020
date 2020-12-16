def parse_rules(rule):
  label, rules = rule.split(':')
  a, b = rules.strip().split(' or ')

  def split_range(rng):
    l, r = rng.split('-')
    return int(l), int(r)

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
  for rule in rules:
    for i in range(rule[0], rule[1]+1):
      valid_tickets[i] = True
  
  total = 0
  for ticket in tickets:
    if ticket not in valid_tickets:
      total += int(ticket)
  return total


def ticket_departure(input):
  rules = {}
  rule_labels = set()
  your_ticket = []
  tickets = []
  valid_tickets = {}
  all_tickets = {}

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
        rule_labels.add(label)
      rules[label].extend(rule)

    if sections == 1:
      your_ticket = list(map(int, line.split(',')))
      tickets.append(your_ticket)

    if sections == 2:
      tickets.append(list(map(int, line.split(','))))

  orders = {}
  for i, _ in enumerate(tickets[0]):
    orders[i] = set(list(rule_labels))


  for label in rules:
    rngs = rules[label]
    valid_tickets[label] = {}
    for rng in rngs:
      lo, hi = rng
      for i in range(lo, hi+1):
        valid_tickets[label][i] = True
        all_tickets[i] = True

  for ticket in tickets:
    for i, no in enumerate(ticket):
      if no not in all_tickets:
        continue
      for label in rules:
        if no not in valid_tickets[label]:
          orders[i].remove(label)

  output = {}
  while bool(orders):
    keys = orders.keys()
    for k in keys:
      if len(orders[k]) == 1:
        key = k
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
    print(ticket_error_rate(f))


def part_two():
  with open('input_16.txt') as f:
    print(ticket_departure(f))

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()