# Two Characters
# https://www.hackerrank.com/challenges/two-characters/problem

from itertools import combinations

n = int(input().strip())
s = input().strip()[:n]
max = 0
s_set = set(s)
length = len(s_set)
if length > 1:
    for c in combinations(s_set, length-2):
        new_s = s
        for ch in c:
            new_s = new_s.replace(ch,'')
        if len([i for i in range(len(new_s) - 1) if new_s[i] == new_s[i + 1]]) == 0:
            if len(new_s) > max: max = len(new_s)
print(max)
