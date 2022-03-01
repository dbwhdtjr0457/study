import sys


n, k = map(int, sys.stdin.readline().split())

numList = list(map(int, sys.stdin.readline().split()))

sumList = [0] * n
sumList[0] = numList[0]
for i in range(1, n):
    sumList[i] = sumList[i - 1] + numList[i]

for _ in range(k):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sumList[j - 1])

    else:
        print(sumList[j - 1] - sumList[i - 2])
