# # 부분 성공
# winLen = int(input()) * 2 + 1
# dataLen = int(input())
# data = input()

# result = 0

# ok = False
# for i in range(dataLen - winLen):
#     if ok == True:
#         if data[i + winLen - 1] != data[i + winLen - 2]:
#             if data[i + winLen - 1] == 'I':
#                 result += 1
#             continue
#     ok = False
#     if data[i] == 'I':
#         ok = True
#         for j in range(i + 1, i + winLen):
#             if data[j] == data[j - 1]:
#                 ok = False
#                 break
#     if ok == True:
#         result += 1

# print(result)

n = int(input())
m = int(input())
data = input()

pattern = 0
i = 1
result = 0
while i < m - 1:
    if data[i - 1] == 'I' and data[i] == 'O' and data[i + 1] == 'I':
        pattern += 1
        if pattern == n:
            result += 1
            pattern -= 1
        i += 1
    else:
        pattern = 0
    i += 1

print(result)
