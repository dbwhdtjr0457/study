import sys
import collections
import heapq


# n = int(input())
# flights = []
# for _ in range(n):
#     flights.append(list(map(int, input().split())))
# start, end, K = map(int, input().split())
n = 13
flights = [[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8], [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64], [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92], [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23], [11, 6, 79], [6, 12, 36], [2, 11, 100], [2, 5, 49], [7, 0, 17], [5, 8, 95], [3, 9, 98], [8, 10, 61], [
    2, 12, 38], [5, 7, 58], [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7], [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90], [0, 5, 43], [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94], [2, 7, 38], [3, 7, 88], [9, 12, 20], [12, 0, 26], [10, 5, 38], [12, 8, 50], [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67], [5, 6, 34], [9, 7, 62], [5, 3, 67]]
start = 10
end = 1
K = 9


def solution(n, flights, start, end, K):
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    Q = [(0, start, K)]

    visited = {}

    while Q:
        price, node, k = heapq.heappop(Q)

        if node == end:
            return price

        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))

    return -1


print(solution(n, flights, start, end, K))


n = 13
flights = [[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8], [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64], [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92], [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23], [11, 6, 79], [6, 12, 36], [2, 11, 100], [2, 5, 49], [7, 0, 17], [5, 8, 95], [3, 9, 98], [8, 10, 61], [
    2, 12, 38], [5, 7, 58], [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7], [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90], [0, 5, 43], [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94], [2, 7, 38], [3, 7, 88], [9, 12, 20], [12, 0, 26], [10, 5, 38], [12, 8, 50], [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67], [5, 6, 34], [9, 7, 62], [5, 3, 67]]
src = 10
dst = 1
K = 10

graph = collections.defaultdict(list)
INF = float('inf')
K += 1
dist = [[INF] * n for _ in range(K+1)]
for s, e, v in flights:
    graph[s].append((e, v))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start, K))
    dist[K][start] = 0

    while queue:
        d, node, k = heapq.heappop(queue)

        for nxt, val in graph[node]:
            cost = d + val
            if k-1 >= 0 and dist[k-1][nxt] > cost:
                dist[k-1][nxt] = cost
                heapq.heappush(queue, (cost, nxt, k-1))


dijkstra(src)

print(min(list(zip(*dist))[dst]))
