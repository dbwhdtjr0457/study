arr = [False] + [True] * 10000

for i in range(1, 10001):
    num = i
    while num <= 10000:
        newArr = list(map(int, str(num)))
        num = num + sum(newArr)
        if num <= 10000:
            arr[num] = False

for i in range(len(arr)):
    if arr[i] == True:
        print(i)