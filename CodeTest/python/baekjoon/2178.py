from collections import deque


n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]

queue = deque([(0, 0, 1)])
visited[0][0] = True

while queue:
    x, y, count = queue.popleft()
    if x == n - 1 and y == m - 1:
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
            if data[nx][ny] == '1' and not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True                

print(count)