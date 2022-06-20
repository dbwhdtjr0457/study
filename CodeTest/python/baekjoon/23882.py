n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
flag = False

for last in range(n, 0, -1):
    max = 0
    maxIndex = 0
    for i in range(last):
        if max < arr[i]:
            max = arr[i]
            maxIndex = i
    if maxIndex != i:
        arr[maxIndex], arr[i] = arr[i], arr[maxIndex]
        count += 1
        if count == k:
            for num in arr:
                print(num, end = ' ')
            flag = True
            break

if flag == False:
    print(-1)