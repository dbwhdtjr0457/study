n = int(input())
arr = [*map(int, input().split())]

result = [-1] * n

for i in range(n):
    num = arr[i]
    result[i] = max(1, result[i])
    for j in range(i, n):
        if arr[j] > num:
            result[j] = max(result[i] + 1, result[j])

print(max(result))
