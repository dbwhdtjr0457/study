from collections import deque
import sys


size = int(sys.stdin.readline())

data = []

for _ in range(size):
    data.append(sys.stdin.readline())

visited = [[False] * size for _ in range(size)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    if visited[x][y]:
        return False

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        mx, my = queue.popleft()
        for i in range(4):
            if 0 <= mx + dx[i] <= size - 1 and 0 <= my + dy[i] <= size - 1:
                if not visited[mx + dx[i]][my + dy[i]] and data[mx][my] == data[mx + dx[i]][my + dy[i]]:
                    queue.append((mx + dx[i], my + dy[i]))
                    visited[mx + dx[i]][my + dy[i]] = True

    return True


def bfs_odd(x, y):
    if visited[x][y]:
        return False

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        mx, my = queue.popleft()
        for i in range(4):
            if 0 <= mx + dx[i] <= size - 1 and 0 <= my + dy[i] <= size - 1:
                if not visited[mx + dx[i]][my + dy[i]] and (data[mx][my] == data[mx + dx[i]][my + dy[i]] or (data[mx][my] == "R" and data[mx + dx[i]][my + dy[i]] == "G") or (data[mx][my] == "G" and data[mx + dx[i]][my + dy[i]] == "R")):
                    queue.append((mx + dx[i], my + dy[i]))
                    visited[mx + dx[i]][my + dy[i]] = True

    return True


normCount = 0
oddCount = 0
for i in range(size):
    for j in range(size):
        if bfs(i, j):
            normCount += 1

visited = [[False] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        if bfs_odd(i, j):
            oddCount += 1


print(normCount, oddCount)
