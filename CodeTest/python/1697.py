from collections import deque


n, k = map(int, input().split())

visited = [False] * 100001

count = 0
queue = deque()
queue.append((n, count))
visited[n] = True

while queue:
    data, turn = queue.popleft()
    if data == k:
        break
    turn += 1
    if data - 1 >= 0:
        if visited[data - 1] == False:
            queue.append((data - 1, turn))
            visited[data - 1] = True
    if data + 1 <= 100000:
        if visited[data + 1] == False:
            queue.append((data + 1, turn))
            visited[data + 1] = True
    if data * 2 <= 100000:
        if visited[data * 2] == False:
            queue.append((data * 2, turn))
            visited[data * 2] = True

print(turn)