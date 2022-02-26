x1, x2, x3, x4, x5 = map(int, input().split())

result = (pow(x1, 2) + pow(x2, 2) + pow(x3, 2) + pow(x4, 2) + pow(x5, 2)) % 10

print(result)