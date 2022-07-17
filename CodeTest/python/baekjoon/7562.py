from collections import deque

def bfs(x, y, maplen, end_x, end_y, visited):
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    while queue:
        x, y, count = queue.popleft()
        if x == end_x and y == end_y:
            return count
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= maplen - 1 and 0 <= ny <= maplen - 1 and not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True


n = int(input())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

for i in range(n):
    maplen = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[False] * maplen for _ in range(maplen)]
    print(bfs(start_x, start_y, maplen, end_x, end_y, visited))