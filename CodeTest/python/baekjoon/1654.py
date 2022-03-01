import sys

# k : 랜선 개수, n : 목표 개수
k, n = map(int, sys.stdin.readline().split())

lineList = []
longest = 0

# 입력 받으면서 제일 짧은 줄 기록
for _ in range(k):
    newLine = int(sys.stdin.readline())
    if longest == 0:
        longest = newLine
    else:
        longest = max([longest, newLine])

    lineList.append(newLine)

# 현재 줄을 제일 짧은 줄 길이로 설정
nowLine = longest + 1

tempLine = 0
result = 0

while True:
    mid = (tempLine + nowLine) // 2

    if mid == tempLine:
        break

    count = 0

    for line in lineList:
        count += line // mid

    if count < n:
        nowLine = mid
    elif count >= n:
        if result == 0:
            result = mid
        else:
            result = max([result, mid])
        tempLine = mid


print(result)
