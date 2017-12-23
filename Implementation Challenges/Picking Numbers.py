# Picking Numbers
# https://www.hackerrank.com/challenges/picking-numbers/problem

n = int(input().strip())
array = [int(i) for i in input().split()][:n]

counts = []
for i in set(sorted(array)):
    counts.append([i, array.count(i)])

answer = 0
for i in range(len(counts)):
    if i < len(counts) - 1:
        if counts[i+1][0] - counts[i][0] <= 1:
            total = counts[i][1] + counts[i+1][1]
            answer = total if total > answer else answer
    answer = counts[i][1] if counts[i][1] > answer else answer
print(answer)
        
