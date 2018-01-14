# Cut the sticks
# https://www.hackerrank.com/challenges/cut-the-sticks/problem

n = int(input().strip())
l = list(map(int, input().split()))[:n]
r = []
while len(l) > 0:
    r.append(len(l))
    l = list(filter(lambda a: a != min(l), l))
print(*r, sep = '\n')
