from collections import deque
import sys


# 길이 : n, 치킨집 개수 : m
n, m = map(int, sys.stdin.readline().split())

# 맵 데이터
mapData = []

# 맵 입력
for _ in range(n):
    mapData.append(list(map(int, sys.stdin.readline().split())))

# 치킨집 위치 파악 및 0으로 설정 ==> mapData에는 치킨집 없는 상태로 만듬
# 가정집 위치 파악
chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if mapData[i][j] == 1:
            houses.append((i, j))
        elif mapData[i][j] == 2:
            chickens.append((i, j))


chooseList = []
index = 0
chickenList = []


def chickenChoose(chooseList, index):
    if len(chooseList) < m:
        for i in range(index, len(chickens)):
            newChooseList = chooseList + [chickens[i]]
            chickenChoose(newChooseList, i + 1)

    elif len(chooseList) == m:
        chickenList.append(chooseList)


chickenChoose(chooseList, index)

finalLength = 0

for chicken in chickenList:
    result = 0

    for house in houses:
        minHouse = 0
        for item in chicken:
            if minHouse == 0:
                minHouse = abs(house[0] - item[0]) + abs(house[1] - item[1])
            else:
                minHouse = min(minHouse, abs(
                    house[0] - item[0]) + abs(house[1] - item[1]))

        result += minHouse

    if finalLength == 0:
        finalLength = result
    else:
        finalLength = min(finalLength, result)


print(finalLength)
