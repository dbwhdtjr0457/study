from collections import deque


m = int(input())
n = int(input())

graph = [[] for _ in range(m+1)]

for i in range(n):
    input1, input2 = map(int, input().split())
    graph[input1].append(input2)
    graph[input2].append(input1)

visited = [False] * (m+1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)

print(visited.count(True) - 1)
