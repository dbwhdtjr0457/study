n = int(input())

arr = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        arr[i] = min(arr[i], arr[i - j * j] + 1)

print(arr[n])