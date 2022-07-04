n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(len(arr[-1])):
        if i == 0:
            maxNum = arr[i][0]
        if i != 0:
            if j == 0:
                arr[i][j] += arr[i - 1][0]
                if i == len(arr[-1]) - 1:
                    maxNum = max(maxNum, arr[i][j])
            elif j == len(arr[-1]) - 1:
                arr[i][j] += arr[i - 1][-1]
                if i == len(arr[-1]) - 1:
                    maxNum = max(maxNum, arr[i][j])
            else:
                arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])
                if i == len(arr[-1]) - 1:
                    maxNum = max(maxNum, arr[i][j])
    
print(maxNum)