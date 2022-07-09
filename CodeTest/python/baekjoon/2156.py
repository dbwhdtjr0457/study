import sys

n = int(input())


arr = [0]
dp = [0] * (n + 1)
for i in range(1, n + 1):
    arr.append(int(sys.stdin.readline().strip()))
    if i == 1:
        dp[1] = arr[1]
    elif i == 2:
        dp[2] = dp[1] + arr[2]
    elif i == 3:
        dp[3] = max(dp[2], arr[2] + arr[3], dp[1] + arr[3])
    else:
        dp[i] = max(dp[i - 1], dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i])

print(dp)
print(dp[n])