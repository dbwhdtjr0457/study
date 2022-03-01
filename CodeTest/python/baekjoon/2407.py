n, k = map(int, input().split())


pacList = []
pacList.append(1)

for i in range(1, n + 1):
    pacList.append(pacList[i - 1] * i)

print(pacList[n]//(pacList[k] * pacList[n - k]))
