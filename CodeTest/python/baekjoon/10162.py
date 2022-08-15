n = int(input())
a = n // 300
n = n - a * 300
b = n // 60
n = n - b * 60
c = n // 10
n = n - c * 10

if n == 0:
    print(a, b, c)
else:
    print(-1)