n = int(input())
arr1 = list(map(int, input().split()))

arr2 = sorted(set(arr1))

dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr1:
    print(dic[i], end = ' ')