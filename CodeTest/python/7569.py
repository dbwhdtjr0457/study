# m : 가로, n : 세로, h : 높이
from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())

# 토마토판 구현
data = [[] for _ in range(h)]

# 토마토판 초기 데이터 입력
for i in range(h):
    for j in range(n):
        data[i].append(list(map(int, sys.stdin.readline().split())))

# x, y, z 방향 구현
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(x, y, z):
    queue = deque()

    # 처음 값 queue에 저장
    queue.append((x, y, z))

    while queue:
        # queue 맨 왼쪽 값 빼오며 저장
        a, b, c = queue.popleft()

        for i in range(6):
            # 안 익은 토마토가 있을 경우
            nextA = a + dx[i]
            nextB = b + dy[i]
            nextC = c + dz[i]

            if nextA >= 0 and nextA <= h - 1 and nextB >= 0 and nextB <= n - 1 and nextC >= 0 and nextC <= m - 1:
                if data[nextA][nextB][nextC] == 0 or data[nextA][nextB][nextC] > data[a][b][c] + 1:
                    data[nextA][nextB][nextC] = data[a][b][c] + 1
                    queue.append((nextA, nextB, nextC))


# bfs 실행
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                bfs(i, j, k)

# 실행 후 결과 도출
solved = True
maxNum = 1
for i in range(h):
    for j in range(n):
        for k in range(m):
            maxNum = max([maxNum, data[i][j][k]])
            if data[i][j][k] == 0:
                solved = False
                break

if solved:
    print(maxNum - 1)
else:
    print(-1)
