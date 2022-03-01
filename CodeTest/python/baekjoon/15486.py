# import sys
# sys.setrecursionlimit(1000000)

# n = int(sys.stdin.readline())

# schedule = [(0, 0)]
# for _ in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     schedule.append((x, y))

# dp = [-1] * (n + 1)


# def solution(k, profit):
#     if k > n:
#         return profit

#     elif k + schedule[k][0] - 1 > n:
#         return profit

#     if dp[k] == -1:
#         dp[k] = max(solution(k + schedule[k][0], profit + schedule[k][1]), solution(k + 1, profit))

#     return dp[k]


# print(solution(1, 0))


# N = int(input())
# table = [0] * (N + 1)
# for i in range(1, N+1):
#     t, p = map(int, input().split())
#     if i + t - 1 < N + 1:
#         table[i + t - 1] = max(table[i + t - 1], table[i - 1] + p)
#     table[i] = max(table[i], table[i - 1])
#     print(table)

# print(table[-1])
