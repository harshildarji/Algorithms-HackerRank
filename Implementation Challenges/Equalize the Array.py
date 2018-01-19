# Equalize the Array
# https://www.hackerrank.com/challenges/equality-in-a-array/problem

n = int(input().strip())
a = list(map(int, input().split()))[:n]
print(n - a.count(max(set(a), key = a.count)))
