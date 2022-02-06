
import sys


n = int(sys.stdin.readline())

data = set(map(int, sys.stdin.readline().split()))

k = int(sys.stdin.readline())

findList = list(map(int, sys.stdin.readline().split()))

for num in findList:
    if num in data:
        print(1)
    else:
        print(0)
