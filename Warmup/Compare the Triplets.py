# Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
alice = bob = 0
for i in range(0, 3):
    if a[i] > b[i]:
        alice += 1
    elif a[i] < b[i]:
        bob += 1
print("%s %s" % (alice, bob))
