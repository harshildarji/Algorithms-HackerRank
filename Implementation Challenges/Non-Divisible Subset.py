# Non-Divisible Subset
# https://www.hackerrank.com/challenges/non-divisible-subset/problem

n, k = map(int, input().split())
a = list(map(int,input().split()))[:n]

counts = [0] * k
for number in a: counts[number % k] += 1
count = min(counts[0], 1)
for i in range(1, k//2+1):
    if i != k - i: count += max(counts[i], counts[k-i])
if k % 2 == 0: count += 1
print(count)
