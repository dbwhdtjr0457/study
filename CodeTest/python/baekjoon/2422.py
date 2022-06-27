import sys


n, m = map(int, input().split())

ban = set()
for i in range(m):
    num1, num2 = map(int, sys.stdin.readline().split())
    if num1 > num2:
        ban.add((num2, num1))
    else:
        ban.add((num1, num2))

result = 0
for i in range(3, n + 1):
    for j in range(2, i):
        for k in range(1, j):
            if (k, j) not in ban and (k, i) not in ban and (j, i) not in ban:
                result += 1

print(result)