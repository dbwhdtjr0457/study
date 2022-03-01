from collections import deque


n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)

visited = [False for _ in range(n)]

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

result = 0
for i in range(n):
    if not visited[i]:
        bfs(i, graph, visited)
        result += 1

print(result)