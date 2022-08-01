n, m = map(int, input().split())

mapData = []
for _ in range(n):
    temp = list(map(int, input().split()))
    for i in range(1, n):
        temp[i] += temp[i - 1]
    mapData.append(temp)

for i in range(1, n):
    for j in range(n):
        mapData[i][j] += mapData[i - 1][j]

print(mapData)


result = []
for _ in range(m):
    start_x, start_y, end_x, end_y = map(int, input().split())
    temp = mapData[end_x - 1][end_y - 1]
    if start_x > 1:
        temp -= mapData[start_x - 2][end_y - 1]
    if start_y > 1:
        temp -= mapData[end_x - 1][start_y - 2]
    if start_x > 1 and start_y > 1:
        temp += mapData[start_x - 2][start_y - 2]
    result.append(temp)

print(*result, sep='\n')