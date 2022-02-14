def solution(n, k, div):
    if k == 1:
        return n % div
    r = solution(n, k // 2, div)
    if k % 2 == 0:
        return r * r % div
    else:
        return r * r * n % div


n, k, div = map(int, input().split())

print(solution(n, k, div))
