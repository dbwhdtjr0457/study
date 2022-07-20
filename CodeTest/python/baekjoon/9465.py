n = int(input())

for _ in range(n):
    k = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    dp = [[0] * k for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if k > 1:
        dp[0][1] = arr[0][1] + dp[1][0]
        dp[1][1] = arr[1][1] + dp[0][0]
    for i in range(2, k):
        dp[0][i] = arr[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = arr[1][i] + max(dp[0][i - 1], dp[0][i - 2])
    print(max(dp[0][k - 1], dp[1][k - 1]))