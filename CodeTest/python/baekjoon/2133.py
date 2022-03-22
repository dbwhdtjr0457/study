n = int(input())

arr = [0] * (n + 2)

arr[2] = 3

for i in range(4, n + 2, 2):
    arr[i] += arr[i - 2] * 3
    for j in range(2, i - 3, 2):
        arr[i] += arr[j] * 2
    arr[i] += 2

print(arr[n])
