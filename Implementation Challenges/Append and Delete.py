# Append and Delete
# https://www.hackerrank.com/challenges/append-and-delete/problem

s, t = input().strip(), input().strip()
k = int(input().strip())
for i in reversed(range(1, k + 1)):
    if s == t[:len(s)] and len(t) - len(s) == i or len(s) == 0:
        break
    s = s[:-1]
print("Yes" if len(t) - len(s) <= i else "No")
