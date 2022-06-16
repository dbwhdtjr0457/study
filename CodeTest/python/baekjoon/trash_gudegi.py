n = int(input())


def matrix_mult(A, B):
    temp = [[0] * (len(A)) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                temp[i][k] += A[i][j] * B[j][k] % 1000
    return temp


def matrix_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        temp = matrix_pow(A, n//2)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(A, n-1)
        return matrix_mult(temp, A)


if n == 1:
    k = int(input())
    result = 0
    for i in range(1, k + 1):
        num = i * (i + 1) / 2
        result += num

    print(int(result))

elif n == 4:
    a, b = map(int, input().split())
    print(a + b)

elif n == 7:
    N, B = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    for row in matrix_pow(matrix, B):
        for item in row:
            print(item, end=' ')
        print()

elif n == 8:
    print("절대신")
