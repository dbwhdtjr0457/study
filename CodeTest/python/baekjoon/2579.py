n = int(input())

stairList = []
for _ in range(n):
    stairList.append(int(input()))


dp = [-1] * (n + 1)

dp[0] = stairList[0]
dp[1] = stairList[0] + stairList[1]
dp[2] = max(stairList[0] + stairList[2], stairList[1] + stairList[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2] + stairList[i], dp[i - 3] +
                stairList[i - 1] + stairList[i])

print(dp[n - 1])
