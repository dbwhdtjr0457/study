from collections import deque


n, m = map(int, input().split())

shortCut = {}
for _ in range(n + m):
    x, y = map(int, input().split())
    shortCut[x] = y

def bfs():
    visited = [False] * 101
    queue = deque([(1, 0)])

    while queue:
        x, y = queue.popleft()
        y += 1
        for i in range(1, 7):
            newX = x + i
            
            if newX < 100 and not visited[newX]:
                if newX in shortCut:
                    newX = shortCut[newX]
                queue.append((newX, y))
                visited[newX] = True
            elif newX == 100:
                return y

print(bfs())