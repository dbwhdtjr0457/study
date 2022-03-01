from cmath import inf
from collections import deque


n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]


for _ in range(m):
    x, y = map(int, input().split())
    data[x].append((y, 1))
    data[y].append((x, 1))

def bfs(start):
    result = 0

    visited = [False] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        num, dist = queue.popleft()
        dist += 1
        for i in data[num]:
            if not visited[i[0]]:
                result += dist
                queue.append((i[0], dist))
                visited[i[0]] = True
    return (start, result)

minNum = (inf, inf)
for i in range(1, n + 1):
    newResult = bfs(i)
    if minNum[1] > newResult[1]:
        minNum = newResult

print(minNum[0])