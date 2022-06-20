n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
newArr = arr1[:]

newArr.sort()
location = {}
for i, num in enumerate(arr1):
    location[num] = i

flag = False
for i in range(n - 1, -1, -1):
    if arr1 == arr2:
        flag = True
        break
    if newArr[i] != arr1[i]:
        temp1, temp2 = arr1[i], newArr[i]
        arr1[location[newArr[i]]] = arr1[i]
        location[arr1[i]] = location[newArr[i]]
        arr1[i] = newArr[i]
        location[newArr[i]] = arr1[i]

if flag:
    print(1)
else:
    print(0)