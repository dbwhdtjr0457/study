n = int(input())

data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))

count = 0
endDate = (3, 1)
temp = (3, 1)
able = True
ans = False
data.sort()

for i, date in enumerate(data):

    if (date[0], date[1]) > temp:
        able = False
        break
    elif (date[0], date[1]) > endDate and (date[2], date[3]) > temp:
        count += 1
        endDate = temp
        temp = (date[2], date[3])
        if (date[2], date[3]) > (11, 30):
            count += 1
            ans = True
            break

    elif (date[0], date[1]) <= endDate:
        if (date[2], date[3]) > (11, 30):
            count += 1
            ans = True
            break
        else:
            temp = max(temp, (date[2], date[3]))

if able and ans:
    print(count)
else:
    print(0)
