#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  sack = []
  fsort = sorted(items,reverse=True, key = lambda k: k[2] )
  sort = sorted(fsort,key = lambda k: k[1])
  i = 0
  total = 0
  for item in sort:
    print('{} to be added'.format(item))
    if i + item[1] < capacity:  
      i = item[1] + i
      total = total + item[2]
      sack.append(item)
      print('{} added to sack.Sack currently has {} and is at capacity {}'.format(item,sack,i))
    else:
      pass
  return total

    
    
    


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