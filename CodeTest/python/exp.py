# # A번
# from itertools import permutations

# n = int(input())

# cost = list(map(int, input().split()))
# discount = [[] for _ in range(n)]

# for i in range(n):
#     k = int(input())
#     for _ in range(k):
#         discount[i].append(tuple(map(int, input().split())))

# minNum = float('inf')

# for i in permutations([k for k in range(n)], n):
#     tempCost = cost[:]
#     result = 0
#     for j in i:
#         result += tempCost[j]
#         for item in discount[j]:
#             x, y = item[0] - 1, item[1]
#             tempCost[x] -= y
#             if tempCost[x] <= 0:
#                 tempCost[x] = 1
#     minNum = min(minNum, result)

# print(minNum)

# ## 이왜맞?

# B번


n, q = map(int, input().split())

mapData = [0] + list(map(int, input().split()))

mapLink = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    mapLink[x].append(y)
    mapLink[y].append(x)

resultList = []


def dfs(start, end, result):

    result += str(mapData[start])
    if start == end:
        print(int(result) % 1000000007)
        return
    visited[start] = True

    for item in mapLink[start]:
        if item == end:
            print(int(result + str(mapData[item])) % 1000000007)
            return
        if not visited[item]:
            dfs(item, end, result)


for _ in range(q):
    visited = [False for _ in range(n + 1)]
    start, end = map(int, input().split())
    result = ''
    dfs(start, end, result)


# # C번


# from collections import defaultdict
# from itertools import combinations

# n = int(input())
# dict = defaultdict(list)
# data = input()

# for i, char in enumerate(data):
#     if char == "W" or char == "H" or char == "E":
#         dict[char].append(i)

# for char in dict:
#     dict[char].reverse()

# result = 0
# prevResult = 0
# prev = float('inf')
# for i in dict['W']:
#     for j in dict['H']:
#         if j > i and j < prev:
#             for k in range(len(dict['E'])):
#                 eTemp = -1
#                 if dict['E'][k] <= j:
#                     eTemp = k
#                     break
#             if eTemp != -1:
#                 for t in range(2, len(dict['E'][:eTemp]) + 1):
#                     result += len(list(combinations(dict['E'][:eTemp], t)))
#             else:
#                 for t in range(2, len(dict['E']) + 1):
#                     result += len(list(combinations(dict['E'], t)))
#     result += prevResult
#     prev = i
#     prevResult = result

# print(result % 1000000007)

# # 개선 C번

# from collections import Counter
# n = int(input())
# data = input()
# dict = Counter(data)

# tempW = 0
# tempE = dict['E']

# result = 0

# for char in data:
#     if char == 'W':
#         tempW += 1
#     elif char == 'E':
#         tempE -= 1
#     elif char == 'H':
#         result += tempW * (pow(2, tempE) - tempE - 1)

# print(result % 1000000007)
# # 맞 았 다 !
