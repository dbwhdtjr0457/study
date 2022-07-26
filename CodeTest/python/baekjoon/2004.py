# 1번
# n, m = map(int, input().split())

# count_two = 0
# count_five = 0
# for i in range(m):
#     temp = n - i
#     while (not(temp % 2)):
#         temp //= 2
#         count_two += 1
#     while (not(temp % 5)):
#         temp //= 5
#         count_five += 1
# for i in range(1, m + 1):
#     temp = i
#     while (not(temp % 2)):
#         temp //= 2
#         count_two -= 1
#     while (not(temp % 2)):
#         temp //= 5
#         count_five -= 1

# print(min(count_two, count_five))

# 2번
# n, m = map(int, input().split())

# count_zero = 0
# result = 1
# for i in range(m):
#     result *= n - i
# for i in range(m):
#     result //= i + 1
# while (not(result % 10)):
#     count_zero += 1
#     result //= 10
# print(count_zero)

n, m = map(int, input().split())

def count2(x):
    count = 0
    while (x):
        count += x // 2
        x //= 2
    return count

def count5(x):
    count = 0
    while (x):
        count += x // 5
        x //= 5
    return count

count_2 = count2(n) - count2(n - m) - count2(m)
count_5 = count5(n) - count5(n - m) - count5(m)

print(min(count_2, count_5))