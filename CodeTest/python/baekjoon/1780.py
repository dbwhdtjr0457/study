import sys

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

countMinusOne = 0
countZero = 0
countOne = 0


def solution(n, x, y):
    global countMinusOne, countZero, countOne
    checkNum = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if checkNum != data[i][j]:
                checkNum = -2
                break

    if checkNum == -2:
        cutLen = n // 3
        solution(cutLen, x, y)
        solution(cutLen, x + cutLen, y)
        solution(cutLen, x + (cutLen * 2), y)
        solution(cutLen, x, y + cutLen)
        solution(cutLen, x + cutLen, y + cutLen)
        solution(cutLen, x + (cutLen * 2), y + cutLen)
        solution(cutLen, x, y + (cutLen * 2))
        solution(cutLen, x + cutLen, y + (cutLen * 2))
        solution(cutLen, x + (cutLen * 2), y + (cutLen * 2))

    elif checkNum == -1:
        countMinusOne += 1
    elif checkNum == 0:
        countZero += 1
    elif checkNum == 1:
        countOne += 1


solution(n, 0, 0)
print(countMinusOne)
print(countZero)
print(countOne)
