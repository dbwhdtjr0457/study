n = int(input())


def binary(n):
    if n == 0:
        return ''
    if n % 2 == 0:
        return binary(n // 2) + '0'
    else:
        return binary(n // 2) + '1'


def solution(n):

    countOne = binary(n).count('1')

    for i in range(n + 1, 1000001):
        if binary(i).count('1') == countOne:
            answer = i
            break

    return answer


print(solution(n))
