arr = list(map(int, input().split()))
fullArr = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(fullArr[i] - arr[i], end=' ')