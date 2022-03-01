import sys


n, k = map(int, sys.stdin.readline().split())

dropList = []
for _ in range(n):
    dropList.append(int(sys.stdin.readline()))


dp = [-1] * (n + 1)
stateList = [1, 2]


def solution(t, k, state, count):
    if k == 0:
        for i in range(t, n):
            if state == dropList[i]:
                count += 1
        return count

    if t > n - 1:
        return count

    else:
        if state == dropList[t]:
            return solution(t + 1, k, state, count + 1)
        else:
            return max(solution(t + 1, k, state, count), solution(t + 1, k - 1, stateList[state % 2], count + 1))


print(solution(0, k, 1, 0))
