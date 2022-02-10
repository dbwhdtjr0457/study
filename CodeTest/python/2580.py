n = int(input())

numList = [0] * 4

numList[1] = 1
numList[2] = 2
numList[3] = 4


def solution(n):
    if n <= 3:
        return numList[n]
    else:
        return solution(n - 1) + solution(n - 2) + solution(n - 3)


for _ in range(n):
    num = int(input())
    print(solution(num))
