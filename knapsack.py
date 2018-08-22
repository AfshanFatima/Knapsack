#!/usr/bin/python

import sys
from collections import namedtuple
from itertools import combinations
from operator import itemgetter

Item = namedtuple('Item', ['index', 'size', 'value'])

def brute_force_solver(items, capacity):
  """
  Refined Brute Force Method
  Uses `max` built-in function to find greatest value
  in combos generator expression
  """
  combos = (
    combo
    for index, item in enumerate(items)
    for combo in combinations(items, index)
  )

  def maximum_value(combo):
    value = sum([x[2] for x in combo])
    size = sum([x[1] for x in combo])
    return (value, ) if size <= capacity else (0, 0)

  knapsack = max(combos, key=maximum_value)

  indices = [ index for index,_,_ in knapsack ]
  value = sum([ value for _,_,value in knapsack ])
  size = sum([ size for _,size,_ in knapsack ])

  return f"Value: {value}\nSize: {size}\nChosen: {indices}"


def knapsack_solver(items, capacity):
  possible = []
  combos = []
  total_size = 0
  total_value = 0
  total_index = 0

  for row in range(len(items)):
    for comb in combinations(items, row):
      combos.append(comb)

  for index in range(len(combos)):
    combo = itemgetter(index)(combos)
    sizes = [x[1] for x in combo]
    if sum(sizes) < capacity:
      possible.append(combo)

  for combo in possible:
    indexes = [x[0] for x in combo]
    sizes = [x[1] for x in combo]
    value = sum([x[2] for x in combo])
    if total_value < value:
      total_value = value
      total_size = sum(sizes)
      total_index = indexes

  return f"Value: {total_value}\nSize: {total_size}\nChosen: {total_index}"

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
    # print(brute_force_solver(items, capacity))
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
