n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

result = -1
for i in range(1, n):
    loc = i - 1
    newItem = arr[i]
    while (0 <= loc and newItem < arr[loc]):
        arr[loc + 1] = arr[loc]
        count += 1
        if count == k:
            result = arr[loc + 1]
            break
        loc -= 1
    if (loc + 1 != i):
        arr[loc + 1] = newItem
        count += 1
        if count == k:
            result = arr[loc + 1]
            break

print(result)