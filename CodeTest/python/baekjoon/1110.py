n = int(input())
origin = n

result = 0
while True:
    if n < 10:
        n *= 11
    else:
        new = ((n // 10 + n % 10) % 10) + ((n % 10) * 10)
        n = new
    result += 1
    if origin == n:
        print(result)
        break
