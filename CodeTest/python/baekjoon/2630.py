n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

countOne = 0
countZero = 0

def solution(x, y, length):
    global countOne, countZero

    state = data[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if data[i][j] != state:
                state = -1
                break
    
    if state == -1:
        length = length // 2
        solution(x, y, length)
        solution(x, y + length, length)
        solution(x + length, y, length)
        solution(x + length, y + length, length)
    
    elif state == 0:
        countZero += 1
    
    elif state == 1:
        countOne += 1

solution(0, 0, n)

print(countZero)
print(countOne)