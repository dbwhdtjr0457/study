n, k = map(int, input().split())

data = [*map(int, input().split())]

left, right = 0, 0
countOdd = 0
countEven = 0
result = 0

while right < n:
    if data[right] % 2 == 0:
        countEven += 1
        result = max(result, countEven)
    elif data[right] % 2 == 1:
        countOdd += 1

    if countOdd > k:
        while countOdd > k:
            if data[left] % 2 == 0:
                countEven -= 1
            elif data[left] % 2 == 1:
                countOdd -= 1
            left += 1

    right += 1

print(result)
