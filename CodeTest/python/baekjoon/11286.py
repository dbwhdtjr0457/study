import heapq
import sys


n = int(input())
posArr = []
negArr = []

for _ in range(n):
    k = int(sys.stdin.readline())

    if k > 0:
        heapq.heappush(posArr, k)
    elif k < 0:
        heapq.heappush(negArr, -k)
    else:
        if posArr:
            if negArr:
                if posArr[0] >= negArr[0]:
                    print(-heapq.heappop(negArr))

                else:
                    print(heapq.heappop(posArr))
            else:
                print(heapq.heappop(posArr))
        elif negArr:
            print(-heapq.heappop(negArr))
        else:
            print(0)
