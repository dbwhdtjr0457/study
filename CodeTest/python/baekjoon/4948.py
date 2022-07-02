while True:
    n = int(input())
    if n == 0:
        break
    boolArr = [False, False] + [True] * (2 * n - 1)
    
    result = 0
    for i in range(2, 2 * n + 1):
        if boolArr[i]:
            for j in range(2 * i, 2 * n + 1, i):
                boolArr[j] = False
            if i > n:
                result += 1
    print(result)