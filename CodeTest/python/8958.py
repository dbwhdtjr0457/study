import sys


n = int(input())

for _ in range(n):
    string = sys.stdin.readline()
    count = 0
    result = 0
    for i in range(len(string) - 1):
        if string[i] == 'O':
            count += 1
        elif string[i] == 'X':
            count = 0
        result += count
    print(result)