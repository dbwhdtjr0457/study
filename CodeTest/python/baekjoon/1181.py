import sys


n = int(input())

arr = []
for i in range(n):
    item = sys.stdin.readline().strip()
    if (len(item), item) not in arr:
        arr.append((len(item), item))

arr.sort(key=lambda x : (x[0], x[1]))

for item in arr:
    print(item[1])