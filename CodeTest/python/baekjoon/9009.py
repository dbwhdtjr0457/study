n = int(input())

arr = [1, 2]
for i in range(2, 46):
    arr.append(arr[i - 2] + arr[i - 1])

for i in range(n):
    resultArr = []
    temp = 0
    k = int(input())
    while (k):
        for j in range(46):
            if arr[j] <= k:
                temp = arr[j]
            else:
                break
        k -= temp
        resultArr.append(temp)
    resultArr.reverse()
    print(*resultArr)
