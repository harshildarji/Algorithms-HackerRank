# Birthday Chocolate
# https://www.hackerrank.com/challenges/the-birthday-bar/problem

n = int(input().strip())
s = [int(i) for i in input().split()][:n]
d, m = map(int, input().split())
ways = 0
for i in range(n):
    if sum(s[i:i+m]) == d:
           ways += 1
print(ways)
