import sys

n = int(input())

for i in range(1, n + 1):
    a = sys.stdin.readline()
    print(str(i) + ". " + a)