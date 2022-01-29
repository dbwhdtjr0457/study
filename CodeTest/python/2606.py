m = int(input())
n = int(input())

graph = [[] for _ in range(m+1)]

for i in range(n):
    input1, input2 = map(int, input().split())
    graph[input1].append(input2)
    graph[input2].append(input1)

visited = [False] * m

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

print(visited.count(True) - 1)
