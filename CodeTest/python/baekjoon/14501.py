n = int(input())

schedule = [(0, 0)]

for _ in range(n):
    x, y = map(int, input().split())
    schedule.append((x, y))

dp = [0] * (n + 1)

for i in range(1, n + 1):

    x, y = schedule[i]
    if i + x - 1 <= n:
        dp[i + x - 1] = max(dp[i + x - 1], dp[i - 1] + y)
    dp[i] = max(dp[i], dp[i - 1])
    print(i)
    print(dp)
