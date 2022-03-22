n, m = map(int, input().split())

arr = [*map(int, input().split())]

left, right = 0, 0
numSum = 0
result = 0
numSum += arr[0]

while True:
    if numSum == m:
        result += 1
        right += 1
        if right == len(arr):
            break
        numSum += arr[right]
    elif numSum < m:
        right += 1
        if right == len(arr):
            break
        numSum += arr[right]
    elif numSum > m:
        if left < right:
            numSum -= arr[left]
            left += 1
        else:
            left += 1
            right += 1
            if right == len(arr):
                break
            numSum = arr[right]

print(result)
