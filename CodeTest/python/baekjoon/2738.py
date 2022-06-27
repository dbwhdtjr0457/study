n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    newArr = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] += newArr[j]

for item in arr:
    print(*item)
