# Staircase
# https://www.hackerrank.com/challenges/staircase/problem

n = int(input().strip())
for i in range(0, n):
    print(" " * (n-(i+1)) + "#" * (i+1))
