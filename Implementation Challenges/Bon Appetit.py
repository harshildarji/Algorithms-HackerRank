# Bon Appétit
# https://www.hackerrank.com/challenges/bon-appetit/problem

n, k = map(int, input().split())
items = [int(i) for i in input().split()][:n]
anna = int(input().strip())
items.pop(k)
if anna == (sum(items) // 2): print('Bon Appetit')
else: print(anna - (sum(items) // 2))
