from collections import deque


n = int(input())

arr = deque()
result = 0

for _ in range(n):
    k = int(input())
    if not arr:
        arr.append(k)
    else:
        while True and arr:
            if arr[-1] <= k:
                arr.pop()
            else:
                break
        result += len(arr)
        arr.append(k)

print(result)
