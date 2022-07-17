n = int(input())

arr = [0] + [*map(int, input().split())]

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        for j in range(1, n + 1):
            dp[j] = arr[i] * j
    else:
        for j in range(i, n + 1):
            dp[j] = max(dp[j], arr[i] + dp[j - i])

print(dp[n])