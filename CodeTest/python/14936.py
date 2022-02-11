n, m = map(int, input().split())

evenNum = n // 2
oddNum = n - evenNum
threeNum = n // 3
if n > threeNum * 3:
    threeNum += 1

result = 1
if evenNum <= m:
    result += 1
if oddNum <= m:
    result += 1
if threeNum <= m:
    result += 1
if evenNum + oddNum <= m:
    result += 1
if evenNum + threeNum <= m:
    result += 1
if oddNum + threeNum <= m:
    result += 1
if evenNum + oddNum + threeNum <= m:
    result += 1

if n == 1:
    if m == 0:
        print(1)
    else:
        print(2)
elif n == 2:
    if m == 0:
        print(1)
    if m == 1:
        print(3)
    else:
        print(4)
else:
    print(result)
