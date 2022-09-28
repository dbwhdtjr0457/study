a, b, c, d = map(int, input().split())
num = (b // d) * (c // d)

print(min(a, num))