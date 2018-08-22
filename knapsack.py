#!/usr/bin/python

import sys
from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):

  single_item_list = [(item,) for item in items]
  double_item_list = list(combinations(items, 2))
  triple_item_list = list(combinations(items, 3))
  quadruple_item_list = list(combinations(items, 4))
  quintuple_item_list = list(combinations(items, 5))
  sextuple_item_list = list(combinations(items, 6))
  septuple_item_list = list(combinations(items, 7))
  octuple_item_list = list(combinations(items, 8))
  nonuple_item_list = list(combinations(items, 9))
  decuple_item_list = list(combinations(items, 10))

  master_item_list = []
  master_item_list.append(single_item_list)
  master_item_list.append(double_item_list)
  master_item_list.append(triple_item_list)
  master_item_list.append(quadruple_item_list)
  master_item_list.append(quintuple_item_list)
  master_item_list.append(sextuple_item_list)
  master_item_list.append(septuple_item_list)
  master_item_list.append(octuple_item_list)
  master_item_list.append(nonuple_item_list)
  master_item_list.append(decuple_item_list)

  
  pass

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
