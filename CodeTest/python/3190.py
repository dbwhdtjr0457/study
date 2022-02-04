# 한 변 길이
from collections import deque


size = int(input())
# 변 * 변 맵 구현
mapData = [[0] * size for _ in range(size)]

# 사과 개수
appleNum = int(input())

# 사과는 맵에 2로 표시
for _ in range(appleNum):
    x, y = map(int, input().split())
    mapData[x-1][y-1] = 2

# 방향 전환 횟수
turnNum = int(input())

# 방향 전환 정보 저장 리스트
turnList = deque()

# 방향 전환 정보 저장
for _ in range(turnNum):
    x, y = input().split()
    turnList.append((x, y))


# 초기 위치 (0, 0), 뱀 존재 위치는 1로 표시
mapData[0][0] = 1


# 시간 변수 설정
sec = 0

# 방향 설정 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dir = 1

# 뱀 머리, 몸 설정
head = (0, 0)
body = deque()
body.append(head)

# 첫 번째 방향 전환 정보 저장
turnTime, turnType = turnList.popleft()

# 게임 시작
while True:

    sec += 1
    # 머리를 다음 위치로 이동
    head = (head[0] + dx[dir], head[1] + dy[dir])
    

    # 머리가 맵 밖으로 이동 시 종료
    if head[0] <= -1 or head[0] >= size or head[1] <= -1 or head[1] >= size:
        break

    # 머리 위치를 몸 정보에 추가
    body.append(head)

    # 이동한 칸 숫자 확인
    if mapData[head[0]][head[1]] == 0:
        x, y = body.popleft()
        mapData[x][y] = 0
    elif mapData[head[0]][head[1]] == 1:
        break

    # 이동한 머리 위치에 정보 추가
    mapData[head[0]][head[1]] = 1

    # 회전 정보 참조
    if sec == int(turnTime):
        if turnType == 'L':
            dir = (dir - 1) % 4
        elif turnType == 'D':
            dir = (dir + 1) % 4

        if turnList:
            turnTime, turnType = turnList.popleft()


print(sec)
