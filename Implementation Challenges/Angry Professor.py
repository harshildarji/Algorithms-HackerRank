# Angry Professor
# https://www.hackerrank.com/challenges/angry-professor/problem

t = int(input().strip())
canceled = []
for _ in range(t):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))[:n]
    if len(list(filter(lambda x: x <= 0, times))) < k: canceled.append('YES')
    else: canceled.append('NO')
print(*canceled, sep = '\n')
