from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False] * (F + 1)

def bfs(visited):
    queue = deque([(S, 0)])

    result = False

    while queue:
        floor, count = queue.popleft()
        if floor == G:
            print(count)
            result = True
            break
        else:
            if floor + U <= F and visited[floor + U] == False:
                visited[floor + U] = True
                queue.append((floor + U, count + 1))
            if floor - D >= 1 and visited[floor - D] == False:
                visited[floor - D] = True
                queue.append((floor - D, count + 1))
    
    if not result:
        print("use the stairs")

bfs(visited)