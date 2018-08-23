#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver_greedy(items, capacity):
  
  bag = [ (item.size/ item.value, item.value, item.size) for item in items ]
  sorted_bag = sorted( bag, key=lambda i: i[0] )

  starting_capacity = 0
  curr_value = 0

  print(bag)
  print("========================")
  print(sorted_bag)

  # loop through list to see if it fits
  for i in sorted_bag:
    if starting_capacity + i[2] < capacity:

      starting_capacity += i[2]
      curr_value += i[1]
  return curr_value 



def knapsack_solver(items, capacity):
  def helper(items, capacity, curr_val):
  # 2. Base 1: we have no more items in the pile
    # print(items)
    if not items:
      print("current value", curr_val)
      return curr_val
      # 3. Base 2: we have one item left in the pile.
      # Check to see if it fits in our bag's remaining capacity. If it does, take it. Otherwise discard it.

    # if len(items) == 1:
    #   if items[0].size < capacity:
    #     items[0]
    #   else:
    #     return 0



    elif items[0].size > capacity:
      return helper(items[1:], capacity, curr_val)

    else:

      r1 = helper(items[1:], capacity - items[0].size, curr_val + items[0].value)
      r2 = helper(items[1:], capacity, curr_val)

      return max(r1, r2)
  return helper(items, capacity, 0)




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
    # print(knapsack_solver(items, capacity))
    print(knapsack_solver_greedy(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')