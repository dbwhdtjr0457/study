import sys
sys.setrecursionlimit(100000)

data = int(input())

countList = [0] * 1001
countList[0] = 1
countList[1] = 1
countList[2] = 2

def countRec(n):
    if countList[n] == 0:
        countList[n] = countRec(n - 1) + countRec(n - 2)
        return countRec(n - 1) + countRec(n - 2)
    else:
        return countList[n]


print(countRec(data) % 10007)