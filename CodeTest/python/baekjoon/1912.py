n = int(input())
arr = list(map(int, input().split()))

maxNum = arr[0]

curr = 0

for item in arr:
    curr += item
    maxNum = max(maxNum, curr)
    if curr < 0:
        curr = 0

print(maxNum)