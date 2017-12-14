# Simple Array Sum
# https://www.hackerrank.com/challenges/simple-array-sum/problem

n = int(input().strip())
values = [int(i) for i in input().strip().split()][:n]
print(sum(values))
