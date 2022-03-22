# 메모리 초과
# import heapq


# n = int(input())

# data = [[] * n for _ in range(n)]
# for _ in range(n):
#     row = [*map(int, input().split())]

#     for i in range(len(row)):
#         heapq.heappush(data[i], -row[i])

# for i in range(n):
#     k = 0
#     popNum = data[0][0]
#     for j in range(1, n):
#         if popNum > data[j][0]:
#             k = j
#             popNum = data[j][0]
#     result = -heapq.heappop(data[k])
#     if i == n - 1:
#         print(result)

import heapq

n = int(input())

data = []

for _ in range(n):
    row = [*map(int, input().split())]
    for item in row:
        heapq.heappush(data, item)
        if len(data) > n:
            heapq.heappop(data)

result = heapq.heappop(data)
print(result)
