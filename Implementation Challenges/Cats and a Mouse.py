# Cats and a Mouse
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

q = int(input().strip())
result = []
for i in range(q):
    points = list(map(int, input().split()))
    if abs(points[2] - points[0]) > abs(points[2] - points[1]): result.append('Cat B')
    elif abs(points[2] - points[0]) < abs(points[2] - points[1]): result.append('Cat A')
    else: result.append('Mouse C')
print(*result, sep = '\n')
