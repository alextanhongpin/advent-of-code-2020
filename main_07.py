import re

def parse_rules(rules):
  bag_rules = {}
  for rule in rules:
    # Strip whitespaces, and remove dot `.` character.
    rule = rule.strip()[:-1]
    big_bag, bags = rule.split(' contain ')
    big_bag = big_bag.replace('bags', 'bag').strip()
    small_bags = bags.split(', ')

    bag_rules[big_bag] = {}
    for small_bag in small_bags:
      if (matches := re.findall('[0-9]+', small_bag)):
        number_of_bags = int(matches[0])

        # Remove the number of bags.
        small_bag = small_bag.replace(matches[0], '').strip()

        # Convert plurals to singular for uniform keys.
        small_bag = small_bag.replace('bags', 'bag') 

        bag_rules[big_bag][small_bag] = number_of_bags
      else:
        bag_rules[big_bag][small_bag] = 0

  return bag_rules

def bag_contained_by(rules, target='shiny gold bag'):
  bag_rules = parse_rules(rules)

  targets = [target]
  parent_bags = {}
  while len(targets):
    target = targets.pop()
    for k, v in bag_rules.items():
      if target in v:
        parent_bags[k] = True
        targets.append(k)
  return len(parent_bags)

def bag_contains(rules, target='shiny gold bag'):
  bag_rules = parse_rules(rules)

  targets = [target]
  count = 0
  while len(targets):
    target = targets.pop()
    if target in bag_rules:
      for bag, n in bag_rules[target].items():
        count += n
        targets.extend([bag] * n)
  return count

def part_one():
  with open('input_07.txt') as f:
    print(bag_contained_by(f)) # 252

def part_two():
  with open('input_07.txt') as f:
    print(bag_contains(f)) # 35487

def main():
  part_one()
  part_two()

if __name__ == '__main__':
  main()