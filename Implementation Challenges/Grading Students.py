# Grading Students
# https://www.hackerrank.com/challenges/grading/problem

n = int(input().strip())
grades = []
for i in range(n):
    grade = int(input().strip())
    rounded = int(round(grade/5.0)*5.0)
    if rounded > grade and rounded - grade < 3 and rounded >= 40:
        grade = rounded
    grades.append(grade)
print(*grades, sep = '\n')
