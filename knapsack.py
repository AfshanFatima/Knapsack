#!/usr/bin/python

import sys
from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  num_of_combinations = 1
  final_size = 0
  final_value = 0
  final_items = ""
  while num_of_combinations <= len(items):
    for combination in combinations(items, num_of_combinations):
      total_size = 0
      total_value = 0
      selected_items = ""
      for item in combination:
        total_size += item.size
        total_value += item.value
        selected_items += str(item.index) + ", "
      selected_items.rstrip(", ")
      if total_size > capacity or total_value <= final_value:
        continue
      else:
        final_size = total_size
        final_value = total_value
        final_items = selected_items
    num_of_combinations += 1
  print("Items to Select: {}".format(final_items))
  print("Total cost: {}".format(final_size))
  print("Total value: {}".format(final_value))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()
    knapsack_solver(items, capacity)
  else:
    print('Usage: knapsack.py [filename] [capacity]')