# Sock Merchant
# https://www.hackerrank.com/challenges/sock-merchant/problem

n = int(input().strip())
socks = sorted([int(i) for i in input().split()][:n])
count = 0
for i in socks:
    count += socks.count(i)//2
    socks = socks[socks.count(i):]
print(count)
