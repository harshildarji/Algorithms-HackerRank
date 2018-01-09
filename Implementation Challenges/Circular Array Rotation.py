# Circular Array Rotation
# https://www.hackerrank.com/challenges/circular-array-rotation/problem

n, k, q = map(int, input().split())
a = list(input().split())[:n]
b = a[-(k%n):] + a[:-(k%n)]
l = []
for i in range(q): l.append(b[int(input().strip())])
print(*l, sep = '\n')
