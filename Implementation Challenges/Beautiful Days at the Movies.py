# Beautiful Days at the Movies
# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

i, j, k = map(int, input().split())
count = 0
for i in range(i, j + 1):
    if (i - int(str(i)[::-1])) % k == 0: count += 1
print(count)
