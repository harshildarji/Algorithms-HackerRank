# Find Digits
# https://www.hackerrank.com/challenges/find-digits/problem

l = []
for _ in range(int(input().strip())):
    n = int(input().strip())
    a = list(map(int, str(n)))
    count = 0
    for i in a:
        if i != 0 and n % i == 0: count += 1
    l.append(count)
print(*l, sep = '\n')
