# n = int(input())
# data = []

# for _ in range(n):
#     data.append(tuple(map(int, input().split())))

# data.sort()
# print(data)

# def solution(index, count):
#     count += 1
#     k = data[index][1]

#     nextAble = False
#     for i in range(index + 1, len(data)):
#         if data[i][0] >= k:
#             nextAble = True
#             nextIndex = i
#             break
#     if nextAble == True:

#         return max(solution(i, count) for i in range(nextIndex, len(data)))
#     else:
#         return count


# print(max(solution(i, 0) for i in range(len(data))))

n = int(input())
data = []

for _ in range(n):
    data.append(tuple(map(int, input().split())))

data.sort(key=lambda x: (x[1], x[0]))

index = 0
count = 0
while True:
    count += 1
    next = False
    for i in range(index + 1, len(data)):
        if data[i][0] >= data[index][1]:
            next = True
            index = i
            break
    if not next:
        break

print(count)
