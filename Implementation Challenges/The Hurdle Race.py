# The Hurdle Race
# https://www.hackerrank.com/challenges/the-hurdle-race/problem

n, k = map(int, input().split())
h = [int(i) for i in input().split()][:n]
print(max(h)-k if max(h) > k else 0)
