# Breaking the Records
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

n = int(input().strip())
records = ([int(i) for i in input().split()][:n])
highest = lowest = records[0]
high = low = 0
for i in records:
    if i not in range(lowest, highest):
        if i > highest: highest = i; high += 1
        elif i < lowest: lowest = i; low += 1
print(high, low)
