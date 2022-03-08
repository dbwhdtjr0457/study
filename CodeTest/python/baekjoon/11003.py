from collections import deque


N, L = map(int, input().split())
data = [*map(int, input().split())]

queue = deque()

for i in range(N):
    while True:
        if queue and queue[-1][1] >= data[i]:
            queue.pop()
        else:
            break

    queue.append((i, data[i]))
    if queue[0][0] < i - L + 1:
        queue.popleft()

    print(queue[0][1], end=' ')
