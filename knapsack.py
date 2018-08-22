#!/usr/bin/python

import sys
from collections import namedtuple
from itertools import combinations as combinations

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  sorted_items = sorted(items, key=lambda x: x[2]/x[1], reverse=True)
  for i in sorted_items:
    print(i)
  counter = 0
  size = 0
  knapsack = []
  while size <= capacity and counter < len(sorted_items):
    for i in sorted_items:
      if i[1] + size <= capacity:
        size += i[1]
        print(size)
        knapsack.append(i)
        print('Knapsack:', knapsack)
      counter += 1
  return knapsack

  # counter = 0
  # new_knapsack_size = 0
  # new_knapsack_value = 0
  # best_knapsack_value = 0
  # best_knapsack = []
  # new_knapsack = []
  # comb_list = [x for l in range(1, len(items)) for x in combinations(items, l)]
  # print(comb_list)
  # for c in comb_list:
  #   for i in c:
  #     new_knapsack_size += i[1]
  #     new_knapsack_value += i[2]
  #   if new_knapsack_size <= capacity and new_knapsack_value > best_knapsack_value:
  #     best_knapsack = c
  #     best_knapsack_value = new_knapsack_value
  #   else:
  #     new_knapsack_size = 0
  #     new_knapsack_value = 0
  # return best_knapsack





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
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')