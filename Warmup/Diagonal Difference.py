# Diagonal Difference
# https://www.hackerrank.com/challenges/diagonal-difference/problem

n = int(input().strip())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

sum1 = sum2 = 0
for i in range(len(matrix)):
    sum1 += matrix[i][i]
    sum2 += matrix[i][n-1-i]
print(abs(sum1-sum2))
