from collections import deque


n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    data[y].append(x)

result = [[] for _ in range(n)]

def bfs(k, visited):
    count = 0
    queue = deque([k])
    visited[k] = True

    while queue:
        i = queue.popleft()
        for num in data[i]:
            if not visited[num]:
                count += 1
                queue.append(num)
                visited[num] = True

    return count



for i in range(1, n + 1):
    visited = [False] * (n + 1)
    result[bfs(i, visited)].append(i)

for i in range(n - 1, -1, -1):
    if len(result[i]) > 0:
        result[i].sort()
        for item in result[i]:
            print(item, end = ' ')

        break