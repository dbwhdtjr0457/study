from collections import deque
import copy

n, m = map(int, input().split())

mapdata = []

for i in range(n):
    row = input().split()
    mapdata.append(row)

# 1. 벽을 세워본다.
# 2. 바이러스를 퍼트린다. 
# 3. 안 퍼진 개수를 센다.
# 4. 가능한 벽 세우기에 대해서 이 모든 걸 다 시뮬레이션 해본다
# 5. 안 퍼진 곳이 가장 큰 값을 출력한다.

result = 0
#1. 
def make_wall(count):
    global result

    if count == 3:
        
        mapcopy = copy.deepcopy(mapdata)
        for i in range(n):
            for j in range(m):
                if mapcopy[i][j] == '2':
                    bfs(mapcopy, i, j)
        
        # 3. 
        zero_count = 0
        for row in mapcopy:
            zero_count += row.count('0')
        result = max(result, zero_count)

    else:
        for i in range(n):
            for j in range(m):
                if mapdata[i][j] == '0':
                    mapdata[i][j] = '1'
                    make_wall(count + 1)
                    mapdata[i][j] = '0'

# 2. 
def bfs(map, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque([(x, y)])

    visited = [[False] * m for _ in range(n)]

    visited[x][y] = True

    while queue:
        
        x1, y1 = queue.popleft()

        for i in range(4):
            newX, newY = x1 + dx[i], y1 + dy[i]
            if 0 <= newX <= n - 1 and 0 <= newY <= m - 1:
                if not visited[newX][newY] and map[newX][newY] == '0':
                    map[newX][newY] = '2'
                    visited[newX][newY] = True
                    queue.append((newX, newY))

make_wall(0)

print(result)


