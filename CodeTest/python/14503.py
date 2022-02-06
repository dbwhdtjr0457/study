# 맵 크기
m, n = map(int, input().split())

# 현 위치, 바라보는 방향
x, y, dir = map(int, input().split())

# 맵 초기화
mapData = []

# 맵 입력
for _ in range(m):
    mapData.append(list(map(int, input().split())))

# 방향 설정 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소하는 칸 수
count = 0

# 청소 시작
while True:
    # 현재 칸 청소
    if mapData[x][y] == 0:
        mapData[x][y] = 2
        count += 1

    # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    if mapData[x + dx[(dir - 1) % 4]][y + dy[(dir - 1) % 4]] == 0:
        dir = (dir - 1) % 4
        x += dx[dir]
        y += dy[dir]
    else:
        able = False
        for i in range(4):
            if mapData[x + dx[i]][y + dy[i]] == 0:
                able = True
                
        # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
        if able == False:
            # 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
            if mapData[x + dx[(dir - 2) % 4]][y + dy[(dir - 2) % 4]] == 1:
                break

            x += dx[(dir - 2) % 4]
            y += dy[(dir - 2) % 4]

        # 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        else:
            dir = (dir - 1) % 4

print(count)