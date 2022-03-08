rep = int(input())

for _ in range(rep):
    data = {}
    n = int(input())
    for _ in range(n):
        x, y = input().split()
        if y not in data:
            data[y] = 0
        data[y] += 1
    result = 1
    for item in data:
        result *= (data[item] + 1)
    result -= 1

    print(result)
