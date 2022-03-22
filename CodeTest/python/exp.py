n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append([*map(int, input().split())])

print(data)
result = 0
for row in data:
    result += row.count(0)

print(result)
