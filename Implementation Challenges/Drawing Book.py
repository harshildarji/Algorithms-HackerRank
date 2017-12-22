# Drawing Book
# https://www.hackerrank.com/challenges/drawing-book/problem

n, p = int(input().strip()), int(input().strip())
print(min(p//2, ((n-p)//2 if n % 2 else (n - p + 1)//2)))
