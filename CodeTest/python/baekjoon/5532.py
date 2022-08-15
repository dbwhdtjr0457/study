l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c:
    a1 = a // c + 1
else:
    a1 = a // c

if b % d:
    b1 = b // d + 1
else:
    b1 = b // d

print(l - max([a1, b1]))