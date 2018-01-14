# Sherlock and Squares
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

import math
l = []
for _ in range(int(input().strip())):
    a, b = map(int, input().split())
    l.append(math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1)))
print(*l, sep = '\n')
