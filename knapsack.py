#!/usr/bin/python

import sys
from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['index', 'size', 'value'])

# Recursive solution
def recur_knapsack_solver(items, cap):
  def knapsack_helper(capacity, no_of_items, weight_lst, val_lst):
    if capacity == 0 or no_of_items == 0:
      return 0
    elif weight_lst[no_of_items - 1] > capacity:
      return knapsack_helper(capacity, no_of_items - 1, weight_lst, val_lst)
    else:
      return max(val_lst[no_of_items - 1] + knapsack_helper(capacity - weight_lst[no_of_items - 1], \
                 no_of_items - 1, weight_lst, val_lst), \
                 knapsack_helper(capacity, no_of_items - 1, weight_lst, val_lst))

  w_lst = [item.size for item in items]
  v_lst = [item.value for item in items]
  print("weight list: {}".format(w_lst))
  print("value list: {}".format(v_lst))
  print("no of items: {}".format(len(items)))
  return knapsack_helper(cap, len(items), w_lst, v_lst)

# functional solution using itertools combinations
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

# Solve using value / size ratio
def ratio_knapsack_solver(items, capacity):
  ratio_lst = [i.value/i.size for i in items]

  count = 0
  cost = 0
  combos = []

  while count < len(ratio_lst):
    max_ratio = max(ratio_lst)
    max_ratio_idx = ratio_lst.index(max_ratio)
    a_item = items[max_ratio_idx]
    if a_item.size <= capacity - cost:
      combos.append(a_item)
      cost += a_item.size
    items.remove(a_item)
    ratio_lst.remove(max_ratio)

  final_items = ''
  for item in sorted(combos):
    final_items += str(item.index) + ","
  final_items.rstrip(",")

  final_size = 0
  for item in combos:
    final_size += item.size

  final_value = 0
  for item in combos:
    final_value += item.value

  print("Items to Select: {}".format(final_items))
  print("Total cost: {}".format(final_size))
  print("Total value: {}".format(final_value))

#Memoization
def memo_knapsack_solver(items, capacity):
  cache = [[0] * capacity + 1 for _ in range(len(items))]

  for c in range(1, len(cache) + 1):
    for i in range(len(items)):





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
    # knapsack_solver(items, capacity)
    # print(recur_knapsack_solver(items, capacity))
    ratio_knapsack_solver(items, capacity)
  else:
    print('Usage: knapsack.py [filename] [capacity]')