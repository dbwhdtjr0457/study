import math

x, y = map(float, input().split())
if x != 0:
    nowRate = math.floor(y * 100 / x)


if nowRate >= 99:
    print(-1)
else:
    low = 0
    high = 10000000000000

    while True:
        mid = (low + high) // 2
        if mid == low:
            break

        newRate = math.floor((y + mid) / (x + mid) * 100)

        if newRate >= nowRate + 1:
            high = mid
        elif newRate < nowRate + 1:
            low = mid

    if math.floor((y + low) / (x + low) * 100) == nowRate + 1:
        print(low)
    else:
        print(high)
