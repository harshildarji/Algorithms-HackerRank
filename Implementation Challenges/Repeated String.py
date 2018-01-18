# Repeated String
# https://www.hackerrank.com/challenges/repeated-string/problem

s = input().strip()
n = int(input().strip())
print((s.count('a') * (n // len(s))) + s[:(n % len(s))].count('a'))

