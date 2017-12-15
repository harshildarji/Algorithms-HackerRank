# A Very Big Sum
# https://www.hackerrank.com/challenges/a-very-big-sum/problem

n = int(input().strip())
values = [int(i) for i in input().split()][:n]
print(sum(values))
