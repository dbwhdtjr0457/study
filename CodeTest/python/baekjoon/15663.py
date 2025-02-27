N, M = map(int, input().split())

inputList = sorted(list(map(int, input().split())))

visited = [False] * N

def backtracking(idxList):

    if len(idxList) == M:
        print(" ".join(list(map(str, [inputList[i] for i in idxList]))), end=" ")
        print()

    else:
        prev = 0
        for i in range(N):
            if prev != inputList[i] and not visited[i]:
                prev = inputList[i]
                visited[i] = True
                backtracking(idxList + [i])
                visited[i] = False


backtracking([])