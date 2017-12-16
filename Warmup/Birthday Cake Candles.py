# Birthday Cake Candles
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

n = int(input().strip())
heights = sorted([int(i) for i in input().split()][:n], reverse = True)
count = 1
for i in range(1, len(heights)):
    if heights[i] == heights[0]:
        count += 1
print(count)
