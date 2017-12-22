# Counting Valleys
# https://www.hackerrank.com/challenges/counting-valleys/problem

n = int(input().strip())
steps = input().upper()[:n]
valleys = level = 0
for i in steps:
    level += 1 if i == 'U' else -1
    if level == 0 and i == 'U': valleys += 1
print(valleys)
