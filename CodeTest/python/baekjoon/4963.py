from collections import deque


def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= m - 1 and 0 <= ny <= n - 1:
                if not visited[nx][ny] and mapdata[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

resultArr = []
while (True):
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    mapdata = []
    for _ in range(m):
        mapdata.append(list(map(int, input().split())))
    visited = [[False] * n for _ in range(m)]
    result = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and mapdata[i][j] == 1:
                bfs(i, j, visited)
                result += 1
    resultArr.append(result)

for item in resultArr:
    print(item)