a, b = map(int, input().split())
arr = list(map(int, input().split()))
for item in arr:
    print(item - (a * b), end=' ')