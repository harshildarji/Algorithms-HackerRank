# Plus Minus
# https://www.hackerrank.com/challenges/plus-minus/problem

n = int(input().strip())
values = [int(i) for i in input().split()][:n]
positive = negative = zero = 0
for i in range(n):
    if values[i] > 0: positive += 1
    elif values[i] == 0: zero += 1
    else: negative += 1
print("%.6f\n%.6f\n%.6f" % (positive/n, negative/n, zero/n))
