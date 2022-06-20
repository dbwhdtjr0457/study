n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
flag = False
for i in range(n):
    if flag == False:
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
                if count == k:
                    for num in arr:
                        print(num, end = ' ')
                    flag = True
                    break
    else:
        break

if not flag:
    print(-1)