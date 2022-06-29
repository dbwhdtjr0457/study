import sys


n, m, b = map(int, input().split())

mapdata = []
minNum = 256
maxNum = 0
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    minNum = min(minNum, min(arr))
    maxNum = max(maxNum, max(arr))
    mapdata.append(arr)

for i in range(n):
    for j in range(m):
        b += mapdata[i][j] - minNum

result = (float('inf'), None)
while b >= 0 and minNum <= maxNum:
    curr = 0
    for i in range(n):
        for j in range(m):
            if minNum <= mapdata[i][j]:
                curr += (mapdata[i][j] - minNum) * 2
            else:
                curr += (minNum - mapdata[i][j])
    if curr <= result[0]:
        result = (curr, minNum)
    minNum += 1
    b -= n * m

print(*result)