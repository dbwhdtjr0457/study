from collections import deque


n = int(input())
arr = [0] + list(map(int, input().split()))
start, end = map(int, input().split())

queue = deque()

queue.append((start, 0))

visited = [False] * (n + 1)
visited[start] = True
flag = False
while queue:
    curr, num = queue.popleft()
    if curr == end:
        flag = True
        print(num)
        break
    tempCurr = curr
    while tempCurr >= 1:
        tempCurr -= arr[curr]
        if tempCurr >= 1 and not visited[tempCurr]:
            queue.append((tempCurr, num + 1))
            visited[tempCurr] = True
    tempCurr = curr
    while tempCurr <= n:
        tempCurr += arr[curr]
        if tempCurr <= n and not visited[tempCurr]:
            queue.append((tempCurr, num + 1))
            visited[tempCurr] = True

if not flag:
    print(-1)