import sys
sys.setrecursionlimit(10**9)

N = int(input())

tree = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

result = [0] * (N + 1)
result[1] = -1

def dfs(result, parent):
    children = tree[parent]

    for child in children:
        if result[child] == 0:
            result[child] = parent
            dfs(result, child)


dfs(result, 1)

for i in range(2, N + 1):
    print(result[i])
