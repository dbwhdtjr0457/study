from collections import deque


n, m = map(int, input().split())

data = [[-1] * (n + 1) for _ in range(n + 1)]


def bfs(x, y):
    visited = [False] * (n + 1)
    queue = deque([(x, 0)])
    visited[x] = True
    while queue:
        nx, distance = queue.popleft()
        for i, ny in enumerate(data[nx]):
            if not visited[i] and ny != -1:
                if i == y:
                    return distance + ny
                queue.append((i, distance + ny))
                visited[i] = True


for _ in range(n - 1):
    x, y, distance = map(int, input().split())
    data[x][y] = distance
    data[y][x] = distance

for _ in range(m):
    x, y = map(int, input().split())
    print(bfs(x, y))
