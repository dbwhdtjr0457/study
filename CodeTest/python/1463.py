
n = int(input())

dp = [-1] * (n + 1)

count = 0

dp[0] = 0
dp[1] = 0

for i in range(2, n + 1):
    print(dp)
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[int(i / 2)] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[int(i / 3)] + 1)

print(dp[n])
