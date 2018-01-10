# Jumping on the Clouds: Revisited
# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

n, k = map(int, input().split())
c = list(map(int, input().split()))[:n]
E = 100
for i in range(0, n, k):
    if c[i] == 0: E -= 1
    else: E -= 3
print(E)
