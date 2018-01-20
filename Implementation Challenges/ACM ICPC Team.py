# ACM ICPC Team
# https://www.hackerrank.com/challenges/acm-icpc-team/problem

import itertools

n, m = map(int, input().split())
knowledge = []
for _ in range(n):
    knowledge.append(int(input(), 2))

mx = -float('inf')
teams = 0
for p1, p2 in itertools.combinations(range(n), 2):
    combined_topics = bin(knowledge[p1] | knowledge[p2]).count('1')
    if (combined_topics == mx):
        teams += 1
    elif (combined_topics > mx):
        mx = combined_topics
        teams = 1

print(mx, teams, sep='\n')
