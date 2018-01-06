# Save the Prisoner!
# https://www.hackerrank.com/challenges/save-the-prisoner/problem

l = []
for _ in range(int(input().strip())):
    n, m, s = list(map(int, input().strip().split()))
    l.append(((s - 1 + m - 1) % n) + 1)
print(*l, sep = '\n')
