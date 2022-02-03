from collections import deque



def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            if x1 + dx[i] >= 0 and x1 + dx[i] <= m - 1 and y1 + dy[i] >= 0 and y1 + dy[i] <= n - 1:
                if graph[x1 + dx[i]][y1 + dy[i]] == 1:
                    graph[x1 + dx[i]][y1 + dy[i]] = 0
                    queue.append((x1 + dx[i], y1 + dy[i]))


rep = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
countList = []

for _ in range(rep):
    m, n, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1


    count = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                count += 1
                bfs(i, j)


    countList.append(count)

for item in countList:
    print(item)
