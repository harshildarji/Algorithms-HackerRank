# Sequence Equation
# https://www.hackerrank.com/challenges/permutation-equation/problem

n = int(input().strip())
a = list(map(int, input().split()))[:n]
for i in sorted(a): print(a.index(a.index(i)+1)+1)
