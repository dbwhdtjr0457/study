n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a = 1
    b = 2
    for _ in range(3, n + 1):
        temp = b
        b = (a + b) % 15746
        a = temp
    print(b)