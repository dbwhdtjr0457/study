n, num = map(int, input().split())

arr = list(map(int, input().split()))
answer = []

for item in arr:
    if item < num:
        answer.append(item)

print(*answer)