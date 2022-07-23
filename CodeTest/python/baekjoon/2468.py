from collections import deque


n = int(input())
mapdata = []
for _ in range(n):
    mapdata.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, height):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                if mapdata[nx][ny] > height:
                    queue.append((nx, ny))

result = 0
for height in range(0, 101):
    count = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and mapdata[i][j] > height:
                bfs(i, j, visited, height)
                count += 1
    if count == 0:
        break
    result = max(result, count)

print(result)