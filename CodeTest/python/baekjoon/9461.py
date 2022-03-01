n = int(input())

data = [0] * 101
data[1] = 1
data[2] = 1
data[3] = 1
data[4] = 2
data[5] = 2
for i in range(6, 101):
    data[i] = data[i - 5] + data[i - 1]

for _ in range(n):
    print(data[int(input())])
