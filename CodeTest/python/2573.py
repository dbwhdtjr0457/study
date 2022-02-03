from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
m, n = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

def dfs(x, y, visited):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if visited[x][y] == False and graph[x][y] != 0:
        
        visited[x][y] = True
        
        count = 0
        if x >= 1 and graph[x - 1][y] == 0 and visited[x - 1][y] == False:
            count += 1
        if x <= m - 2 and graph[x + 1][y] == 0 and visited[x + 1][y] == False:
            count += 1
        if y >= 1 and graph[x][y - 1] == 0 and visited[x][y - 1] == False:
            count += 1
        if y <= n - 2 and graph[x][y + 1] == 0 and visited[x][y + 1] == False:
            count += 1
        graph[x][y] -= count
        if graph[x][y] < 0:
            graph[x][y] = 0
        
        dfs(x - 1, y, visited)
        dfs(x, y - 1, visited)
        dfs(x + 1, y, visited)
        dfs(x, y + 1, visited)
        return True
    
    return False

# def bfs(x, y, visited):         
#     if visited[x][y] == True:
#         return False

#     queue = deque()
#     queue.append((x, y))

#     while queue:
#         count = 0
#         x, y = queue.popleft()
#         visited[x][y] = True
#         if x >= 1 and originalGraph[x - 1][y] == 0:
#             count += 1
#         elif x >= 1 and originalGraph[x - 1][y] != 0 and not visited[x - 1][y] and queue.count((x - 1, y)) == 0:
#             queue.append((x - 1, y))
#         if x <= m - 2 and originalGraph[x + 1][y] == 0:
#             count += 1
#         elif x <= m - 2 and originalGraph[x + 1][y] != 0 and not visited[x + 1][y] and queue.count((x + 1, y)) == 0:
#             queue.append((x + 1, y))
#         if y >= 1 and originalGraph[x][y - 1] == 0:
#             count += 1
#         elif y >= 1 and originalGraph[x][y - 1] != 0 and not visited[x][y - 1] and queue.count((x, y - 1)) == 0:
#             queue.append((x, y - 1))
#         if y <= n - 2 and originalGraph[x][y + 1] == 0:
#             count += 1
#         elif y <= n - 2 and originalGraph[x][y + 1] != 0 and not visited[x][y + 1] and queue.count((x, y + 1)) == 0:
#             queue.append((x, y + 1))

#         graph[x][y] -= count
#         if graph[x][y] < 0:
#             graph[x][y] = 0
        

#     return True


# year = 0
# while True:
#     visited = [[False] * n for _ in range(m)]
#     num = 0
#     originalGraph = [row[:] for row in graph]

#     for i in range(m):
#         for j in range(n):
#             if originalGraph[i][j] != 0:
#                 if bfs(i, j, visited) == True:
#                     num += 1
#     if num != 1:
#         break

#     year += 1

year = 0
while True:
    visited = [[False] * n for _ in range(m)]
    num = 0

    for i in range(m):
        for j in range(n):
            if dfs(i, j, visited) == True:
                num += 1
    
    if num != 1:
        break

    year += 1

if num == 0:
    print(0)
else:
    print(year)