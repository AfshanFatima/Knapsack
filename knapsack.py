#!/usr/bin/python

import sys
from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  master_item_list = []
  for i in range(len(items)):
    master_item_list.append(list(combinations(items, i+1)))
    

  def solve(master_list, a):
    # print(master_list)
    # print(master_list[1])
    for j in master_list[a]:
      if a == 0:
        if j[0].size <= capacity:
          print(f'INDEX: {j[0].index}')
          print(f'SIZE: {j[0].size}')
          print(f'VALUE: {j[0].value} \n')
      elif a == 1:
        if j[0].size + j[1].size <= capacity:
          print(f'INDEX: {j[0].index}, {j[1].index}')
          print(f'SIZE: {j[0].size + j[1].size}')
          print(f'VALUE: {j[0].value + j[1].value} \n')

      elif a == 2:
        if j[0].size + j[1].size + j[2].size <= capacity:
          print(f'INDEX: {j[0].index}, {j[1].index}, {j[2].index}')
          print(f'SIZE: {j[0].size + j[1].size  + j[2].size}')
          print(f'VALUE: {j[0].value + j[1].value + j[2].value} \n')

      elif a == 3:
        if j[0].size + j[1].size  + j[2].size + j[3].size <= capacity:
          print(f'INDEX: {j[0].index}, {j[1].index}, {j[2].index}, {j[3].index} ')
          print(f'SIZE: {j[0].size + j[1].size + j[2].size + j[3].size}')
          print(f'VALUE: {j[0].value + j[1].value + j[2].value + j[3].value} \n')

      elif a == 4:
        if j[0].size + j[1].size  + j[2].size + j[3].size + j[4].size <= capacity:
          print(f'INDEX: {j[0].index}, {j[1].index}, {j[2].index}, {j[3].index}, {j[4].index}')
          print(f'SIZE: {j[0].size + j[1].size + j[2].size + j[3].size + j[4].size }')
          print(f'VALUE: {j[0].value + j[1].value + j[2].value + j[3].value + j[4].value} \n')
    
    return solve(master_list, a+1)
    # for i in master_list:
    #   for j in master_list[1]:
    #       if j[0].size + j[1].size <= capacity:
    #         print(f'INDEX: {j[0].index}, {j[1].index}')
    #         print(f'SIZE: {j[0].size + j[1].size}')
    #         print(f'VALUE: {j[0].value + j[1].value} \n')
    #   break
    # for i in master_list:
    #   for j in master_list[2]:
    #       if j[0].size + j[1].size + j[2].size <= capacity:
    #         print(f'INDEX: {j[0].index}, {j[1].index}, {j[2].index}')
    #         print(f'SIZE: {j[0].size + j[1].size + j[2].size}')
    #         print(f'VALUE: {j[0].value + j[1].value + j[2].value} \n')
    #   break
    # for i in master_list:
    #   for j in i:
    #     if j[0].size <= capacity:
    #       print(f'CURRENT INDEX: {j[0].index}')
    #       print(f'CURRENT SIZE: {j[0].size}')
    #       print(f'CURRENT VALUE: {j[0].value} \n')
    #   break
    # print(master_list[2])
    #(Item([1,2,3], 42+42+68, 81+42+56))
  print('POTENTIAL SOLUTIONS: \n')
  solve(master_item_list, 0)

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
