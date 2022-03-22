# import sys


# n, k = map(int, input().split())

# arr = []
# for i in range(n):
#     arr.append(int(sys.stdin.readline()))

# result = 0


# def solution(index, count):
#     global result
#     while count < k:
#         if index < n - 1:
#             solution(index + 1, count)
#         count += arr[index]
#         if count == k:
#             result += 1


# solution(0, 0)
# print(result)
# 시간 초과
# dp로 다시 풀어야징~

n, k = map(int, input().split())

arr = []
dp = [0] * (k + 1)
dp[0] = 1

for _ in range(n):
    arr.append(int(input()))

for i in arr:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]

print(dp[k])
