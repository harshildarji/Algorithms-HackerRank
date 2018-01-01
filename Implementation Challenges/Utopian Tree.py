# Utopian Tree
# https://www.hackerrank.com/challenges/utopian-tree/problem

n = int(input().strip())
heights = []
for i in range(n):
    c = int(input().strip())
    height = 1
    for i in range(1, c + 1):
        if i % 2 == 0: height += 1
        elif i % 2 != 0: height *= 2
    heights.append(height)
print(*heights, sep = '\n')
