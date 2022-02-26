import sys


studentNum, compareNum = map(int, input().split())
data = [[0] * (studentNum) for _ in range(studentNum)]

for _ in range(compareNum):
    x, y = map(int, sys.stdin.readline().split())

    data[x - 1][y - 1] = -1
    data[y - 1][x - 1] = 1

for i in range(studentNum):
    for j in range(studentNum):
        for k in range(studentNum):
            if data[j][k] == 0:
                if data[j][i] + data[i][k] == -2:
                    data[j][k] = -1
                    data[k][j] = 1
                elif data[j][i] + data[i][k] == 2:
                    data[j][k] = 1
                    data[k][j] = -1

result = 0
for row in data:
    if row.count(0) == 1:
        result += 1

for row in data:
    print(row)

print(result)