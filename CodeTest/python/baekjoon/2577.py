num = 1

for _ in range(3):
    num *= int(input())

numList = [0] * 10

for i in range(len(str(num))):
    divNum = num % 10
    num = num // 10
    numList[divNum] += 1

for i in numList:
    print(i)