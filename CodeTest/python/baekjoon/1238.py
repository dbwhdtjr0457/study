N, M, X = map(int, input().split())

# 그래프 만들기
graph = [[-1] * (N + 1) for _ in range(N + 1)] 

for _ in range(M):
    start, end, distance = map(int, input().split())
    graph[start][end] = distance

def dijkstra(student):
    distanceTable = [-1] * (N + 1)
    visited = [False] * (N + 1)

    
    distanceTable[student] = 0
    visited[student] = True

    for i, distance in enumerate(graph[student]):
        if distance >= 0 and i != student:
            distanceTable[i] = graph[student][i]

    def getMin(visited):
        flag = True
        result = -1
        minDistance = -1

        for i in range(1, N + 1):
            if not visited[i]:
                flag = False
                if (result == -1 or (distanceTable[i] >= 0 and distanceTable[i] < minDistance)):
                    result = i
                    minDistance = distanceTable[i]

        return result, flag

    while True:
        now, flag = getMin(visited)
        if flag:
            break
        visited[now] = True

        for i in range(1, N + 1):
            if not visited[i] and (graph[now][i] > 0 and (distanceTable[i] < 0 or graph[now][i] + distanceTable[now] < distanceTable[i])):
                distanceTable[i] = graph[now][i] + distanceTable[now]

    return distanceTable

result = None

for i in range(1, N + 1):
    if i != X:
        if result == None:
            result = dijkstra(i)[X] + dijkstra(X)[i]
        else:
            result = max(result, dijkstra(i)[X] + dijkstra(X)[i])

print(result)
