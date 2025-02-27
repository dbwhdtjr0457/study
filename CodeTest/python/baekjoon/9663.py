n = int(input())

mapdata = [0] * n

result = 0

def check_row(row):
    for j in range(row):
        if mapdata[j] == mapdata[row] or abs(mapdata[j] - mapdata[row]) == abs(row - j):
            return False
    return True

def backtracking(row):
    global result

    if row >= n:
        result += 1
        return
    
    else:
        for i in range(n):
            mapdata[row] = i
            if check_row(row):
                backtracking(row + 1)

            


backtracking(0)

print(result)