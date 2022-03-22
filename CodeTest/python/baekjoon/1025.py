import math


n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(input())

result = -1
for i in range(n):
    for j in range(m):
        start = data[i][j]
        if pow(math.floor(math.sqrt(int(start))), 2) == int(start):
            result = max(result, int(start))
        for k in range(n):
            for l in range(m):
                if i != k or j != l:
                    next = data[k][l]
                    dx, dy = k - i, l - j
                    nx, ny = i + dx, j + dy
                    num = start
                    while 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                        num = num + data[nx][ny]
                        if pow(math.floor(math.sqrt(int(num))), 2) == int(num):
                            result = max(result, int(num))
                        nx += dx
                        ny += dy

print(result)
