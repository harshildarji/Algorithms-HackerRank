# Viral Advertising
# https://www.hackerrank.com/challenges/strange-advertising/problem

n = int(input().strip())
count = temp = 2
for i in range(1, n):
    count += (temp * 3) // 2
    temp = (temp * 3) // 2
print(count)
