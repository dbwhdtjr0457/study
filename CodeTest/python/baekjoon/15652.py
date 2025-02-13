n, m = map(int, input().split())

numList = [str(i) for i in range(1, n + 1)]
resultList = []

def backtracking(count, idx):
    if count == m:
        print(" ".join(resultList))

    else:
        for i in range(idx, n):
            resultList.append(numList[i])
            backtracking(count + 1, i)
            resultList.pop()

backtracking(0, 0)