from math import sqrt
from math import floor


n, m = map(int, input().split())

for i in range(n, m + 1):
    flag = True
    for j in range(2, floor(sqrt(i)) + 1):
        if i % j == 0:
            flag = False
            break
    if flag and i >= 2:
        print(i)