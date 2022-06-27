from collections import Counter


n = int(input())
arr = list(map(int, input().split()))
countDict = Counter(arr)
print(countDict[int(input())])