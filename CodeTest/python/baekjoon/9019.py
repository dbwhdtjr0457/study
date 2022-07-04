from collections import deque


n = int(input())

def bfs(x, y, visited):
    queue = deque([(x, "")])
    visited[x] = True
    while queue:
        k, rule = queue.popleft()
        if k == y:
            print(rule)
            break
        temp = (k * 2) % 10000
        if not visited[temp]:
            queue.append((temp, rule + 'D'))
            visited[temp] = True
        temp = k - 1
        if temp == -1:
            temp = 9999
        if not visited[temp]:
            queue.append((temp, rule + 'S'))
            visited[temp] = True
        temp = ('0' * (4 - len(str(k)))) + str(k)
        temp = int(temp[1:] + temp[0])
        if not visited[temp]:
            queue.append((temp, rule + 'L'))
            visited[temp] = True
        temp = ('0' * (4 - len(str(k)))) + str(k)
        temp = int(temp[-1] + temp[:-1])
        if not visited[temp]:
            queue.append((temp, rule + 'R'))
            visited[temp] = True


for i in range(n):
    x, y = map(int, input().split())
    visited = [False] * 10000
    bfs(x, y, visited)