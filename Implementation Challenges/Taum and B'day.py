# Taum and B'day
# https://www.hackerrank.com/challenges/taum-and-bday/problem

r = []
for _ in range(int(input().strip())):
    b, w = map(int, input().split())
    x, y, z = map(int, input().split())
    r.append(min(b * x, b * (y + z)) + min(w * (x + z), w * y))
print(*r, sep = '\n')
