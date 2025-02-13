m, n = map(int, input().split())

numList = [i for i in range(1, m + 1)]
resultList = []

def backtracking(count, idx):
    if count == n:
        for item in resultList:
            print(item, end=" ")
        print()

    else:
        for i in range(idx + 1, m):
            resultList.append(numList[i])
            backtracking(count + 1, i)
            resultList.pop()

backtracking(0, -1)