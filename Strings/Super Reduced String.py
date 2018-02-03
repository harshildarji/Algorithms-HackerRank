# Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem

s = input().strip()
l = []
for i in range(len(s)):
    if not l or s[i] != l[-1]: l.append(s[i])
    else: l.pop()
print(''.join(l) if l else 'Empty String')
