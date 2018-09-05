from itertools import combinations
from collections import namedtuple

Item = namedtuple('Item', ('index', 'size', 'value'))
Items = [Item(1, 10, 20), Item(2, 20, 30), Item(3, 30, 40)]


num_of_combinations = 1
while num_of_combinations <= len(Items):
    for combination in combinations(Items, num_of_combinations):
        sum = 0
        index = ""
        for item in combination:
            sum += item.value
            index += str(item.index) + ", "
        index = index.rstrip(", ")
        print("Sum for index {} is {}".format(index, sum))
    num_of_combinations += 1


