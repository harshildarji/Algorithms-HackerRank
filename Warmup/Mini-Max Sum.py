# Mini-Max Sum
# https://www.hackerrank.com/challenges/mini-max-sum/problem

values = [int(i) for i in input().split()]
print("%s %s" % (sum(sorted(values)[:4]), sum(sorted(values)[1:])))
