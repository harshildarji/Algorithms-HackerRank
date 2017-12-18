# Apple and Orange
# https://www.hackerrank.com/challenges/apple-and-orange/problem

s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apple = [int(i) for i in input().split()][:m]
orange = [int(i) for i in input().split()][:n]
apples = oranges = 0
for i in range(m):
    if (a + apple[i]) in range(s, t + 1):
        apples += 1
for i in range(n):
    if (b + orange[i]) in range(s, t + 1):
        oranges += 1
print('%s\n%s' % (apples, oranges))
