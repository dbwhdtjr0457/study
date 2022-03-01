n = int(input())

def fibo(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)
    else:
        if memo[n - 1] == (-1, -1):
            x1, y1 = fibo(n - 1)
        else:
            x1, y1 = memo[n - 1]
        if memo[n - 2] == (-1, -1):
            x2, y2 = fibo(n - 2)
        else:
            x2, y2 = memo[n - 2]
        memo[n] = (x1 + x2, y1 + y2)
        return (x1 + x2, y1 + y2)
            

for _ in range(n):
    k = int(input())
    if k == 0:
        memo = [(-1, -1)] * 2
    else:
        memo = [(-1, -1)] * (k + 1)
    memo[0] = (1, 0)
    memo[1] = (0, 1)
    x1, x2 = fibo(k)
    print(x1, x2)