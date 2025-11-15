n, k = map(int, input().split())

board = [[0] * n for _ in range(k + 1)]

gymList = []

for i in range(n):
    gym = list(map(int, input().split()))
    gymList.append(gym)

for i in range(n):
    for j in range(1, k + 1):
        if i == 0 and gymList[0][0] <= j:
            board[j][i] = gymList[0][1]
        else:
            newJ = 0
            if gymList[i][0] <= j:
                newJ = board[j - gymList[i][0]][i - 1] + gymList[i][1]
            board[j][i] = max(board[j][i - 1], newJ)

print(board[k][n - 1])