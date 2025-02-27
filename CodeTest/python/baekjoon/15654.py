N, M = map(int, input().split())

numlist = list(map(int, input().split()))

numlist.sort()

def backtracking(idxlist):
    global numlist

    if len(idxlist) == M:
        for idx in idxlist:
            print(numlist[idx], end=" ")
        print()
    
    else:
        for i in range(N):
            if i not in idxlist:
                backtracking(idxlist + [i])

backtracking([])

