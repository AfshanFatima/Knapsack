#!/usr/bin/python

import sys
from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  master_item_list = []
  for i in range(len(items)):
    master_item_list.append(list(combinations(items, i+1)))
    

  def solve(master_list):
    print(master_list[1])

    print('POTENTIAL SOLUTIONS: \n')

    for i in master_list:
      print(f'CURRENT INDEX: {i[4][2].index}')
      print(f'CURRENT SIZE: {i[4][2].size}')
      print(f'CURRENT VALUE: {i[4][2].value}')

    #(Item([1,2,3], 42+42+68, 81+42+56))

  solve(master_item_list)

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
