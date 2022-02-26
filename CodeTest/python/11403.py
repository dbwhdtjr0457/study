n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[j][i] + arr[i][k] == 2:
                arr[j][k] = 1

for row in arr:
    for num in row:
        print(num, end = ' ')
    print()