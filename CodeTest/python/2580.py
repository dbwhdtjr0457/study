import sys


import sys
input = sys.stdin.readline


data = []

for _ in range(9):
    data.append(list(map(int, input().split())))

zeroList = []
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            zeroList.append((i, j))


def solution(n):
    if n == len(zeroList):
        for row in range(9):
            print(*data[row])
        return True

    x = zeroList[n][0]
    y = zeroList[n][1]

    for num in range(1, 10):
        able = True
        for i in range(9):
            if data[x][i] == num or data[i][y] == num:
                able = False

        if able:
            for i in range(x // 3 * 3, x // 3 * 3 + 3):
                for j in range(y // 3 * 3, y // 3 * 3 + 3):
                    if data[i][j] == num:
                        able = False

        if able:
            data[x][y] = num
            if solution(n + 1) == True:
                return True

    data[x][y] = 0


solution(0)
