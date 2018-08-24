#!/usr/bin/python

import sys
import time
from collections import namedtuple
from itertools import combinations as combinations

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  t0=time.time()

  # optimized solution 

  sorted_items = sorted(items, key=lambda x: x[2]/x[1], reverse=True)
  # for i in sorted_items:
  #   print(i)
  counter = 0
  size = 0
  knapsack = []
  while size <= capacity and counter < len(sorted_items):
    for i in sorted_items:
      if i[1] + size <= capacity:
        size += i[1]
        # print(size)
        knapsack.append(i)
        # print('Knapsack:', knapsack)
      counter += 1
  t1 = time.time()
  total = t1-t0
  print("Time Greedy:", total)
  return knapsack

  # brute force solution 
def knapsack_brute(items, capacity):
  t0 = time.time()
  counter = 0
  new_knapsack_size = 0
  new_knapsack_value = 0
  best_knapsack_value = 0
  best_knapsack = []
  new_knapsack = []
  comb_list = [x for l in range(1, len(items)) for x in combinations(items, l)]
  for c in comb_list:
    for i in c:
      new_knapsack_size += i[1]
      new_knapsack_value += i[2]
    if new_knapsack_size <= capacity and new_knapsack_value > best_knapsack_value:
      best_knapsack = c
      best_knapsack_value = new_knapsack_value
    else:
      new_knapsack_size = 0
      new_knapsack_value = 0
  t1 = time.time()
  total = t1 - t0
  print("Time Brute:", total)
  return best_knapsack


  # bottom up solution
def knapsack_recursive(items, capacity):
  t0=time.time()
  def recursive(items, capacity, current_knapsack):
    if len(items) == 0:
      return current_knapsack
    elif items[0].size > capacity:
      return recursive(items[1:], capacity, current_knapsack)

    else:

      r1 = recursive(items[1:], capacity - items[0].size, current_knapsack + items[0].value)
      r2 = recursive(items[1:], capacity, current_knapsack)
      print("r1", r1)
      print("r2", r2)
      print("curr", items)
      return max(r1, r2, key=lambda tup: tup[0])
  t1 = time.time()
  total = t1-t0
  print("Time:", total)
  return recursive(items, capacity, 0)


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
    # print('Best:', knapsack_solver(items, capacity))
    solver_greedy = knapsack_solver(items, capacity)
    # solver_brute = knapsack_brute(items, capacity)
    solver_recursive = knapsack_recursive(items, capacity)
    print("solver_greedy")
    for i in solver_greedy:
      print(i)
    print(solver_recursive)

  else:
    print('Usage: knapsack.py [filename] [capacity]')