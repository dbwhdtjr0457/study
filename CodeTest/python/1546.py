num = int(input())
data = list(map(int, input().split()))

maxNum = max(data)

for i in range(num):
    data[i] = (data[i] / maxNum) * 100

avgNum = 0

for i in range(num):
    avgNum += data[i]

avgNum /= num

print(avgNum)