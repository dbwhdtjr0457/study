n = int(input())

count2 = 0
count5 = 0

for i in range(1, n+1):
    num = i
    while num % 2 == 0:
        num /= 2
        count2 += 1
    while num % 5 == 0:
        num /= 5
        count5 += 1

print(min(count2, count5))
