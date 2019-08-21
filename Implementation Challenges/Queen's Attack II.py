# Queen's Attack II
# https://www.hackerrank.com/challenges/queens-attack-2/problem

def checkSum(board, r, c, dR, dC, n):
    sum = 0
    for i in range(n):
        r += dR
        c += dC

        if r < 0 or r >= n or c < 0 or c>=n:
            return sum

        key = str(r) + "-" + str(c)

        if key in board and board[key] == -1:
            return sum
        else:
            sum += 1

    return sum


n, k = map(int, input().split())
rQueen, cQueen = map(int, input().split())

rQueen -= 1; cQueen -= 1

board = {}

for a0 in range(k):
    rObstacle, cObstacle = map(int, input().split())
    r = rObstacle - 1
    c = cObstacle - 1

    board[str(r) + "-" + str(c)] = -1

dCList = [ -1, -1, -1, 0, 0, 1, 1, 1]
dRList = [ -1, 0, 1, -1, 1, 0, -1, 1]

sum = 0
for i in range(8):
    sum += checkSum(board, rQueen, cQueen, dCList[i], dRList[i], n)
            
print(sum)
