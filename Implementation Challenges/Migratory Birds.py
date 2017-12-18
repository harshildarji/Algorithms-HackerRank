# Migratory Birds
# https://www.hackerrank.com/challenges/migratory-birds/problem

n = int(input().strip())
birds = [int(i) for i in input().split()][:n]
types = [0, 0, 0, 0, 0]

for i in range(n):
    types[birds[i]-1] += 1
print(types.index(max(types))+1)
