import heapq
import sys


n = int(input())
data = []
for _ in range(n):
    k = int(sys.stdin.readline())

    if k == 0:
        if len(data) == 0:
            print(0)
        else:
            print(-heapq.heappop(data))

    else:
        heapq.heappush(data, -k)
