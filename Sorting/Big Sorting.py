# Big Sorting
# https://www.hackerrank.com/challenges/big-sorting/problem

from collections import defaultdict

n = int(input().strip())
array = defaultdict(list)

for i in range(n):
    num = input().strip()
    array[len(num)].append(num)

for key in sorted(array):
    for value in sorted(array[key]):
        print(value)
