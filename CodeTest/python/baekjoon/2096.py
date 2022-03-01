n = int(input())

defaultList = list(map(int, input().split()))
maxResult = defaultList[:]
minResult = defaultList[:]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    max1 = max(maxResult[0], maxResult[1]) + a
    max2 = max(maxResult[0], maxResult[1], maxResult[2]) + b
    max3 = max(maxResult[1], maxResult[2]) + c
    min1 = min(minResult[0], minResult[1]) + a
    min2 = min(minResult[0], minResult[1], minResult[2]) + b
    min3 = min(minResult[1], minResult[2]) + c
    maxResult = [max1, max2, max3]
    minResult = [min1, min2, min3]

maxResult = max(maxResult)
minResult = min(minResult)

print(maxResult, minResult)