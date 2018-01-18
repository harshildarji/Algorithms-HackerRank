# Jumping on the Clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

n = int(input().strip())
c = list(map(int, input().split()))[:n]
jumps = i = 0
while i < (n - 1):
    if (i + 2) <= (n - 1) and c[i + 2] == 0: i += 2
    elif c[i + 1] == 0: i += 1
    jumps += 1
print(jumps)
