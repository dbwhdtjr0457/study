n, k = map(int, input().split())
arr = list(map(int, input().split()))
newArr = arr[:]

newArr.sort()
location = {}
for i, num in enumerate(arr):
    location[num] = i

count = 0
flag = False
for i in range(n - 1, -1, -1):
    if newArr[i] != arr[i]:
        temp1, temp2 = arr[i], newArr[i]
        arr[location[newArr[i]]] = arr[i]
        location[arr[i]] = location[newArr[i]]
        arr[i] = newArr[i]
        location[newArr[i]] = arr[i]
        count += 1
        if count == k:
            flag = True
            print(temp1, temp2)
            break

if not flag:
    print(-1)