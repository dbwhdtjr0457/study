# n = int(input())

# for _ in range(n):
#     result = {"None": ["None", "None"]}
#     duplicate = {}
#     index = "None"
#     inputData = input()
#     for item in inputData:
#         if item == '<':
#             if index != "None":
#                 index = result[index][0]
#         elif item == '>':
#             if result[index][1] != "None":
#                 index = result[index][1]
#         elif item == '-':
#             if len(result) > 1 and index != "None":
#                 result[result[index][0]][1] = result[index][1]
#                 result[result[index][1]][0] = result[index][0]
#                 temp = result[index]
#                 del result[index]
#                 index = temp[0]
#         else:
#             if item not in duplicate:
#                 duplicate[item] = 0
#             duplicate[item] += 1
#             result[(item, duplicate[item])] = [index, result[index][1]]
#             result[result[index][1]][0] = (item, duplicate[item])
#             result[index][1] = (item, duplicate[item])
#             index = (item, duplicate[item])

#     index = "None"
#     while result[index][1] != "None":
#         print(result[index][1][0], end='')
#         index = result[index][1]
#     print()

from collections import deque


n = int(input())

for _ in range(n):
    leftArr = deque()
    rightArr = deque()
    data = input()
    for item in data:
        if item == '<':
            if len(leftArr) > 0:
                x = leftArr.pop()
                rightArr.appendleft(x)
        elif item == '>':
            if len(rightArr) > 0:
                x = rightArr.popleft()
                leftArr.append(x)
        elif item == '-':
            if len(leftArr) > 0:
                leftArr.pop()
        else:
            leftArr.append(item)

    print(''.join(leftArr) + ''.join(rightArr))
