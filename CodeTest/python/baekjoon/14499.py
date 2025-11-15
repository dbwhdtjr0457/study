class Dice:
    u, d, f, b, l, r = 0, 0, 0, 0, 0, 0
    
    def getU(self):
        return self.u

    def getD(self):
        return self.d

    def setD(self, num):
        self.d = num

    
    def rollDown(self):
        self.d, self.f, self.u, self.b = self.b, self.d, self.f, self.u

    def rollUp(self):
        self.d, self.f, self.u, self.b = self.f, self.u, self.b, self.d

    def rollLeft(self):
        self.d, self.l, self.u, self.r = self.l, self.u, self.r, self.d

    def rollRight(self):
        self.d, self.l, self.u, self.r = self.r, self.d, self.l, self.u

n, m, x, y, k = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

cmdList = list(map(int, input().split()))

dxdy = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

dice = Dice()

for i in range(k):
    dx, dy = dxdy[cmdList[i]][0], dxdy[cmdList[i]][1]
    if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1:
        x, y = x + dx, y + dy
        if cmdList[i] == 1:
            dice.rollRight()
        elif cmdList[i] == 2:
            dice.rollLeft()
        elif cmdList[i] == 3:
            dice.rollUp()
        elif cmdList[i] == 4:
            dice.rollDown()
        
        if board[x][y] == 0:
            board[x][y] = dice.getD()
        else:
            dice.setD(board[x][y])
            board[x][y] = 0

        print(dice.getU())