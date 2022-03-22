# import copy


# n, m = map(int, input().split())

# data = []
# for _ in range(n):
#     data.append([*map(int, input().split())])

# visited = [[False] * m for _ in range(n)]

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# minCount = 64


# def solution(data, visited):
#     global minCount
#     newVisited = copy.deepcopy(visited)
#     for i in range(n):
#         for j in range(m):
#             if newVisited[i][j] == False:
#                 newVisited[i][j] = True
#                 if data[i][j] == 1:
#                     for k in range(4):
#                         newData = copy.deepcopy(data)
#                         nx, ny = i, j
#                         while 0 <= nx + dx[k] <= n - 1 and 0 <= ny + dy[k] <= m - 1:
#                             nx += dx[k]
#                             ny += dy[k]
#                             if newData[nx][ny] == 6:
#                                 break
#                             elif newData[nx][ny] == 0:
#                                 newData[nx][ny] = -1
#                         solution(newData, newVisited)

#                 elif data[i][j] == 2:
#                     for k in range(2):
#                         newData = copy.deepcopy(data)
#                         nx1, ny1, nx2, ny2 = i, j, i, j
#                         while 0 <= nx1 + dx[k] <= n - 1 and 0 <= ny1 + dy[k] <= m - 1:
#                             nx1 += dx[k]
#                             ny1 += dy[k]
#                             if newData[nx1][ny1] == 6:
#                                 break
#                             elif newData[nx1][ny1] == 0:
#                                 newData[nx1][ny1] = -1
#                         while 0 <= nx2 + dx[k + 2] <= n - 1 and 0 <= ny2 + dy[k + 2] <= m - 1:
#                             nx2 += dx[k + 2]
#                             ny2 += dy[k + 2]
#                             if newData[nx2][ny2] == 6:
#                                 break
#                             elif newData[nx2][ny2] == 0:
#                                 newData[nx2][ny2] = -1
#                         solution(newData, newVisited)

#                 elif data[i][j] == 3:
#                     for k in range(4):
#                         newData = copy.deepcopy(data)
#                         nx1, ny1, nx2, ny2 = i, j, i, j
#                         while 0 <= nx1 + dx[k] <= n - 1 and 0 <= ny1 + dy[k] <= m - 1:
#                             nx1 += dx[k]
#                             ny1 += dy[k]
#                             if newData[nx1][ny1] == 6:
#                                 break
#                             elif newData[nx1][ny1] == 0:
#                                 newData[nx1][ny1] = -1
#                         while 0 <= nx2 + dx[(k + 1) % 4] <= n - 1 and 0 <= ny2 + dy[(k + 1) % 4] <= m - 1:
#                             nx2 += dx[(k + 1) % 4]
#                             ny2 += dy[(k + 1) % 4]
#                             if newData[nx2][ny2] == 6:
#                                 break
#                             elif newData[nx2][ny2] == 0:
#                                 newData[nx2][ny2] = -1
#                         solution(newData, newVisited)

#                 elif data[i][j] == 4:
#                     for k in range(4):
#                         newData = copy.deepcopy(data)
#                         nx1, ny1, nx2, ny2, nx3, ny3 = i, j, i, j, i, j
#                         while 0 <= nx1 + dx[k] <= n - 1 and 0 <= ny1 + dy[k] <= m - 1:
#                             nx1 += dx[k]
#                             ny1 += dy[k]
#                             if newData[nx1][ny1] == 6:
#                                 break
#                             elif newData[nx1][ny1] == 0:
#                                 newData[nx1][ny1] = -1
#                         while 0 <= nx2 + dx[(k + 1) % 4] <= n - 1 and 0 <= ny2 + dy[(k + 1) % 4] <= m - 1:
#                             nx2 += dx[(k + 1) % 4]
#                             ny2 += dy[(k + 1) % 4]
#                             if newData[nx2][ny2] == 6:
#                                 break
#                             elif newData[nx2][ny2] == 0:
#                                 newData[nx2][ny2] = -1
#                         while 0 <= nx3 + dx[(k + 2) % 4] <= n - 1 and 0 <= ny3 + dy[(k + 2) % 4] <= m - 1:
#                             nx3 += dx[(k + 2) % 4]
#                             ny3 += dy[(k + 2) % 4]
#                             if newData[nx3][ny3] == 6:
#                                 break
#                             elif newData[nx3][ny3] == 0:
#                                 newData[nx3][ny3] = -1

#                         solution(newData, newVisited)

#                 elif data[i][j] == 5:
#                     newData = copy.deepcopy(data)
#                     for k in range(4):
#                         nx, ny = i, j
#                         while 0 <= nx + dx[k] <= n - 1 and 0 <= ny + dy[k] <= m - 1:
#                             nx += dx[k]
#                             ny += dy[k]
#                             if newData[nx][ny] == 6:
#                                 break
#                             elif newData[nx][ny] == 0:
#                                 newData[nx][ny] = -1
#                     solution(newData, newVisited)

#     result = 0
#     for row in data:
#         result += row.count(0)
#     minCount = min(minCount, result)


# solution(data, visited)
# print(minCount)
# --> 응 니 얼굴 시간 초과~
# --> 시간 초과 떠 봐~ 시간 초과된 코드까지 복붙해서 폭탄 제출하면 그만이야~
