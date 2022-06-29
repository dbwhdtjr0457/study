# n = int(input())

# arr = [-1] * (n + 1)

# if n >= 3:
#     arr[3] = 1
# if n >= 5:
#     arr[5] = 1

# for i in range(6, n + 1):
#     if arr[i - 3] == -1 and arr[i - 5] != -1:
#         arr[i] = arr[i - 5] + 1
#     elif arr[i - 3] != -1 and arr[i - 5] == -1:
#         arr[i] = arr[i - 3] + 1
#     elif arr[i - 3] != -1 and arr[i - 5] != -1:
#         arr[i] = min(arr[i - 3], arr[i - 5]) + 1

# print(arr[n])

n = int(input())

fiveNum = n // 5
threeNum = (n - fiveNum * 5) // 3

flag = True
while fiveNum >= 0:    
    if (n - fiveNum * 5) % 3 == 0:
        print(fiveNum + threeNum)
        flag = False
        break
    else:
        fiveNum -= 1
        threeNum = (n - fiveNum * 5) // 3

if flag:
    print(-1)