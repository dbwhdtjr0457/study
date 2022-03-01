n, m = input().split()

a = ''
b = ''

for i in range(len(n) - 1, -1, -1):
    a += n[i]

for i in range(len(m) - 1, -1, -1):
    b += m[i]

a = int(a)
b = int(b)
print(max(a, b))
