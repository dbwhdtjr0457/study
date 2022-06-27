# import sys


# n = int(input())

# for _ in range(n):
#     string = sys.stdin.readline()
#     count = 0
#     result = 0
#     for i in range(len(string) - 1):
#         if string[i] == 'O':
#             count += 1
#         elif string[i] == 'X':
#             count = 0
#         result += count
#     print(result)
import sys

n = int(input())

for _ in range(n):
    string = sys.stdin.readline()
    newDict = {}
    for i in range(len(string)):
        if i == 0 and string[i] == 'O':
                newDict[i] = 1
        elif string[i] == 'O':
            newDict[i] = newDict[i - 1] + 1
        else:
            newDict[i] = 0
    print(sum(newDict.values()))