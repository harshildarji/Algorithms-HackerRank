# Divisible Sum Pairs
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

n, k = map(int, input().split())
values = [int(i) for i in input().split()][:n]
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if (values[i] + values[j]) % k == 0:
            count += 1
print(count)
