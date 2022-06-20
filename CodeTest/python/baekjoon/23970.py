n = int(input())
arr = list(map(int, input().split()))
newArr = list(map(int, input().split()))

count = 0
flag = False
for i in range(n):
    if flag == False:
        for j in range(n - i - 1):
            if arr == newArr:
                flag = True
                break
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    else:
        break

if not flag:
    print(0)
else:
    print(1)