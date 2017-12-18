# Between Two Sets
# https://www.hackerrank.com/challenges/between-two-sets/problem

from functools import reduce
from fractions import gcd

n, m = map(int, input().split())
ai = set([int(i) for i in input().split()][:n])
bi = set([int(i) for i in input().split()][:m])
lcm_ai = reduce(lambda x, y: x*y // gcd(x, y), ai)
gcd_bi = reduce(gcd, bi)
print(sum(1 for x in range(lcm_ai, gcd_bi+1, lcm_ai) if gcd_bi % x == 0))
