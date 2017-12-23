# Picking Numbers
# https://www.hackerrank.com/challenges/picking-numbers/problem

n = int(input().strip())
arr = [int(i) for i in input().split()][:n]

counts = {}
sortedCounts = []
answer = 0

for num in arr:
    counts[num] = counts.get(num, 0) + 1
 
for k,v in sorted(counts.items()):
    sortedCounts.append([k, v])

length = len(sortedCounts)
for i in range(length):
    if i < length - 1:
        if sortedCounts[i + 1][0] - sortedCounts[i][0] < 2:
            totalCount = sortedCounts[i][1] + sortedCounts[i + 1][1]
            answer = totalCount if totalCount > answer else answer
    answer = sortedCounts[i][1] if sortedCounts[i][1] > answer else answer
 
print(answer)
