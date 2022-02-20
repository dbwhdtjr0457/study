n = int(input())

data = []
for _ in range(n):
    data.append(input())


def solution(n, x, y):
    check = data[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != data[i][j]:

                check = -1
                break

    if check == -1:
        print('(', end='')
        n = n // 2
        solution(n, x, y)
        solution(n, x, y + n)
        solution(n, x + n, y)
        solution(n, x + n, y + n)
        print(')', end='')

    elif check == '0':
        print('0', end='')

    elif check == '1':
        print('1', end='')


solution(n, 0, 0)
