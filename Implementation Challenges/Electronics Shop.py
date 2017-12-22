# Electronics Shop
# https://www.hackerrank.com/challenges/electronics-shop/problem

s, n, m = map(int, input().split())
KB = [int(i) for i in input().split()][:n]
USB = [int(i) for i in input().split()][:m]
total = []
if min(KB) + min(USB) > s: print('-1')
else:
    for i in KB:
        for j in USB:
            if i + j <= s: total.append(i + j)
print(max(total))
