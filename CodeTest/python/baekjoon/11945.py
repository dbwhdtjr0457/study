a, b = map(int, input().split())
for i in range(a):
    c = input()
    for j in range(b):
        print(c[b - j - 1], end='')
    print()