# n = int(input())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# newArr = arr1[:]

# newArr.sort()
# location = {}
# for i, num in enumerate(arr1):
#     location[num] = i

# flag = False
# for i in range(n - 1, -1, -1):
#     if newArr[i] != arr1[i]:
#         temp1, temp2 = arr1[i], newArr[i]
#         arr1[location[newArr[i]]] = arr1[i]
#         location[arr1[i]] = location[newArr[i]]
#         arr1[i] = newArr[i]
#         location[newArr[i]] = arr1[i]
#     flag = True
#     for j in range(n):
#         if arr1[j] != arr2[j]:
#             flag = False
#     if flag:
#         break

# if flag:
#     print(1)
# else:
#     print(0)

n = int(input())
arr = list(map(int, input().split()))
newArr = list(map(int, input().split()))

flag = False

for last in range(n, 0, -1):
    if arr == newArr:
        flag = True
        break
    max = 0
    maxIndex = 0
    for i in range(last):
        if max < arr[i]:
            max = arr[i]
            maxIndex = i
    if maxIndex != i:
        arr[maxIndex], arr[i] = arr[i], arr[maxIndex]
    
if flag:
    print(1)
else:
    print(0)