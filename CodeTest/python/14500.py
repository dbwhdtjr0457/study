n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

result = 0

for i in range(n):
    for j in range(m):
        if j <= m - 4:
            result = max(result, data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i][j + 3])
        if j <= m - 3 and i <= n - 2:
            result = max(result, data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i + 1][j + 2], data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i + 1][j + 1], data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i + 1][j], data[i][j] + data[i][j + 1] + data[i + 1][j + 1] + data[i + 1][j + 2], data[i][j] + data[i + 1][j] + data[i + 1][j + 1] + data[i + 1][j + 2])
        if j <= m - 3 and i >= 1:
            result = max(result, data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i - 1][j + 2], data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i - 1][j + 1], data[i][j] + data[i][j + 1] + data[i - 1][j + 1] + data[i - 1][j + 2])
        if j <= m - 2 and i <= n - 3:
            result = max(result, data[i][j] + data[i][j + 1] + data[i + 1][j + 1] + data[i + 2][j + 1], data[i][j] + data[i][j + 1] + data[i + 1][j] + data[i + 2][j], data[i][j] + data[i + 1][j] + data[i + 1][j + 1] + data[i + 2][j + 1], data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 2][j + 1], data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 1][j + 1])
        if j <= m - 2 and i <= n - 2:
            result = max(result, data[i][j] + data[i][j + 1] + data[i + 1][j] + data[i + 1][j + 1])
        if j <= m - 2 and i >= 2:
            result = max(result, data[i][j] + data[i][j + 1] + data[i - 1][j + 1] + data[i - 2][j + 1], data[i][j] + data[i - 1][j] + data[i - 1][j + 1] + data[i - 2][j + 1], data[i][j + 1] + data[i - 1][j] + data[i - 1][j + 1] + data[i - 2][j + 1])
        if i <= n - 4:
            result = max(result, data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 3][j])

print(result)