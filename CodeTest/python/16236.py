from collections import deque


n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, size, count, result):
    visited = [[False] * n for _ in range(n)]

    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    change = False
    saveDist = -2
    ans = (20, 20)

    while queue:
        mx, my, dist = queue.popleft()
        if dist == saveDist + 1:
            break
        for i in range(4):
            nx, ny = mx + dx[i], my + dy[i]
            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and visited[nx][ny] == False:
                if data[nx][ny] == 0 or data[nx][ny] == size:
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
                elif data[nx][ny] < size:
                    change = True
                    if saveDist == -2:
                        saveDist = dist
                    if ans[0] > nx or ans[0] == nx and ans[1] > ny:
                        ans = (nx, ny)

    if change == True:
        count += 1
        if size == count:
            size += 1
            count = 0
        result += saveDist + 1
        nx, ny = ans
        data[nx][ny] = 9
        data[x][y] = 0
        return bfs(nx, ny, size, count, result)
    else:
        return result


OK = True
for i in range(n):
    if OK:
        for j in range(n):
            if data[i][j] == 9:
                print(bfs(i, j, 2, 0, 0))
                OK = False
                break
