from math import floor, sqrt


n = int(input())

dp = [-1] * (n + 1)
dp[0] = 0

for i in range(1, len(dp)):
    if pow(round(sqrt(i)), 2) == i:
        dp[i] = 1
    else:
        k = floor(sqrt(i))
        for j in range(1, k + 1):
            if dp[i] == -1:
                dp[i] = dp[i - pow(j, 2)] + 1
            else:
                dp[i] = min(dp[i], dp[i - pow(j, 2)] + 1)
print(dp[n])
