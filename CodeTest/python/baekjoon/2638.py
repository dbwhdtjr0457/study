from collections import deque


n, k = map(int, input().split())

mapData = []
for _ in range(n):
    mapData.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():

    result = 0
    while True:
        change = False
        visited = [[False] * k for _ in range(n)]
        outside = deque()
        outside.append((0, 0))
        visited[0][0] = True

        while outside:
            outx, outy = outside.popleft()
            for i in range(4):
                outnx, outny = outx + dx[i], outy + dy[i]
                if 0 <= outnx <= n - 1 and 0 <= outny <= k - 1:
                    if mapData[outnx][outny] != 1 and visited[outnx][outny] == False:
                        outside.append((outnx, outny))
                        visited[outnx][outny] = True

            mapData[outx][outy] = 2

        for i in range(n):
            for j in range(k):

                if mapData[i][j] == 1 and visited[i][j] == False:
                    change = True
                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = True

                    while queue:
                        count = 0
                        mx, my = queue.popleft()
                        for t in range(4):
                            nx, ny = mx + dx[t], my + dy[t]
                            if 0 <= nx <= n - 1 and 0 <= ny <= k - 1:
                                if mapData[nx][ny] == 2:
                                    count += 1
                                elif mapData[nx][ny] == 1 and visited[nx][ny] == False:
                                    queue.append((nx, ny))
                                    visited[nx][ny] = True

                        if count >= 2:
                            mapData[mx][my] = 0
        if change == True:
            result += 1
        else:
            break

    return result


print(bfs())
