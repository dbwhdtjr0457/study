m, n = map(int, input().split())

data = []
for i in range(m):
    data.append(input())

count1 = 0
count2 = 0
resultList = []

for i in range(m-7):
    for j in range(n-7):
        for I in range(i, i+8):
            for J in range(j, j+8):
                if (I - i + J - j)% 2 == 0:
                    if data[I][J] != data[i][j]:
                        count1 += 1
                    else:
                        count2 += 1
                elif (I - i + J - j) % 2 == 1:
                    if data[I][J] == data[i][j]:
                        count1 += 1
                    else:
                        count2 += 1
        resultList.append(count1)
        resultList.append(count2)
        count1 = 0
        count2 = 0
print(min(resultList))