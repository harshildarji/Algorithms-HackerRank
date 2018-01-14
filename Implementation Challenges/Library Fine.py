# Library Fine
# https://www.hackerrank.com/challenges/library-fine/problem

r = list(map(int, input().split()))
e = list(map(int, input().split()))
if r[2] > e[2]: print('10000')
elif r[1] > e[1] and r[2] == e[2]: print(500*(r[1]-e[1]))
elif r[0] > e[0] and r[1] == e[1] and r[2] == e[2]: print(15*(r[0]-e[0]))
else: print('0')
