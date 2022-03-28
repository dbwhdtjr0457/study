data = []

for _ in range(4):
    data.append(input())

n = int(input())


for _ in range(n):
    wheel, direction = map(int, input().split())
    temp = direction
    wheel -= 1
    change = [False] * 4
    change[wheel] = True

    if wheel > 0 and data[wheel][6] != data[wheel - 1][2]:
        change[wheel - 1] = True

    for i in range(wheel, 3):
        if change[i]:
            if direction == 1:
                data[i] = data[i][7] + data[i][:7]
            else:
                data[i] = data[i][1:] + data[i][0]

            if direction == 1 and data[i][3] != data[i + 1][6] or direction == -1 and data[i][1] != data[i + 1][6]:
                change[i + 1] = True
                direction = -direction

    if change[3]:
        if direction == 1:
            data[3] = data[3][7] + data[3][:7]
        else:
            data[3] = data[3][1:] + data[3][0]

    direction = -temp
    for i in range(wheel - 1, 0, -1):

        if change[i]:
            if direction == 1:
                data[i] = data[i][7] + data[i][:7]
            else:
                data[i] = data[i][1:] + data[i][0]
            if direction == 1 and data[i][7] != data[i - 1][2] or direction == -1 and data[i][5] != data[i - 1][2]:
                change[i - 1] = True
                direction = -direction
    if wheel > 0 and change[0]:
        if direction == 1:
            data[0] = data[0][7] + data[0][:7]
        else:
            data[0] = data[0][1:] + data[0][0]

print(int(''.join(list(zip(*data[::-1]))[0]), 2))
