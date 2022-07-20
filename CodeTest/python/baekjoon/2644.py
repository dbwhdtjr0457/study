from collections import deque


n = int(input())
target = tuple(map(int, input().split()))
m = int(input())
arr = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [False] * (n + 1)


queue = deque([(target[0], 0)])
visited[target[0]] = True
found = False
while queue:
    curr, result = queue.popleft()
    if curr == target[1]:
        print(result)
        found = True
        break
    for item in arr[curr]:
        if not visited[item]:
            queue.append((item, result + 1))
            visited[item] = True

if not found:
    print(-1)