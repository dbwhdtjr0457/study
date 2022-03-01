n, k = map(int, input().split())
arr = list(map(int, input().split()))

maxNum = 0
for i in range(n):
    if i == 0:
        result = sum(arr[j] for j in range(k))
    else:
        result -= arr[i - 1]
        result += arr[(i + k - 1) % n]
    maxNum = max(maxNum, result)

print(maxNum)