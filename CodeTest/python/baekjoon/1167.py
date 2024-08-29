import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

# 정점 리스트
listV = []

# 트리
tree = [{} for _ in range(n + 1)]

# 입력 받기
for _ in range(n):
    inputList = list(map(int, input().split()))[:-1]
    V = inputList[0]
    treeData = inputList[1:]
    listV.append(V)
    tree[V] = {}
    for i in range(len(treeData) // 2):
        tree[V][treeData[i * 2]] = treeData[i * 2 + 1]


def dfs(V, length):
    global result, visited, max_node
    for key, value in tree[V].items():
        if visited[key] == 0:
            visited[key] = 1
            dfs(key, length + value)
        else:
            if length > result:
                result = length
                max_node = V


# 지름
result = 0

max_node = 0

# "트리에서 임의의 노드에서 최대 거리에 있는 노드는 반드시 트리의 지름의 양 끝점 중 하나이다."

visited = [0] * (n + 1)
visited[1] = 1    
dfs(1, 0)


visited = [0] * (n + 1)
visited[max_node] = 1
dfs(max_node, 0)

print(result)