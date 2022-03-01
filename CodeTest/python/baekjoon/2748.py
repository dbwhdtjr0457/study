import sys


n = int(sys.stdin.readline())

dp = [-1] * (n + 1)


def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if dp[n] == -1:
        dp[n] = solution(n - 1) + solution(n - 2)
    return dp[n]


print(solution(n))
