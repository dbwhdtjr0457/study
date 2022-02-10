from collections import deque


size = int(input())

mapData = []
for _ in range(size):
    mapData.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()

    queue.append((x, y))
    visited[x][y] = True

    count = 1

    while queue:
        mx, my = queue.popleft()
        for i in range(4):
            nx = mx + dx[i]
            ny = my + dy[i]
            if 0 <= nx <= size - 1 and 0 <= ny <= size - 1:
                if mapData[nx][ny] == "1" and visited[nx][ny] == False:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1

    return count


result = []
visited = [[False] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        if mapData[i][j] == "1" and not visited[i][j]:
            result.append(bfs(i, j))

result.sort()

print(len(result))
for item in result:
    print(item)
