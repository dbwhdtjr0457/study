a, b = map(int, input().split())

for i in range(a + 1):
    if a - 2 * i == b:
        print(a - i, i)
        break
    elif a - i < i:
        print(-1)
        break