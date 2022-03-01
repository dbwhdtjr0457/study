cityNum = int(input())
busNum = int(input())
inf = 100000000000

costData = [[inf] * cityNum for _ in range(cityNum)]

for _ in range(busNum):
    start, end, cost = map(int, input().split())
    if costData[start - 1][end - 1] > cost:
        costData[start - 1][end - 1] = cost

for i in range(cityNum):
    for j in range(cityNum):
        for k in range(cityNum):
            if j != k and costData[j][k] > costData[j][i] + costData[i][k]:
                costData[j][k] = costData[j][i] + costData[i][k]

for row in costData:
    for item in row:
        if item == inf:
            print(0, end=' ')
        else:
            print(item, end=' ')
    print()
