import sys
input = sys.stdin.readline

N = int(input())

top = [*map(int, input().split())]
bot = [*map(int, input().split())]
left = [*map(int, input().split())]
right = [*map(int, input().split())]

# 보드판 초기화
graph = [[0]*N for _ in range(N)]


# 보드판 가로, 세로 중복 확인 함수
# input: x
# output: boolean
def graph_check():
    for g in graph:
        s = set()
        for n in g:
            if n == 0 or n not in s:
                s.add(n)
            else:
                return False
    
    for g in [*zip(*graph)]:
        s = set()
        for n in g:
            if n == 0 or n not in s:
                s.add(n)
            else:
                return False
    
    return True


# 해당 행 or 열 보이는 개수 반환 함수
# input: [1, 2, 3, 4]
# out: 해당 배열을 왼쪽에서 봤을 때 보이는 개수(int)
def check(arr):
    max = 0
    count = 0
    for n in arr:
        if max < n:
            count += 1
            max = n
    return count


# 재귀 함수
def func(x, y):
    # 현재 보드판 행, 열에 중복되는 숫자가 있을 경우 돌아가기
    if not graph_check():
        return
    

    # 탐색이 끝났을 경우 실행
    if x >= N or y >= N:

        # 세로 방향 숫자 검증
        for i, g in enumerate([*zip(*graph)]):
            if check(g) != top[i] or check(g[::-1]) != bot[i]:
                return
    
        # 맞으면 출력 후 끝
        print('--')
        for g in graph:
            print(*g)
        sys.exit(0)

    
    # 해당 좌표에서 1~N 돌리기
    for i in range(1, N+1):

        # 해당 좌표에 숫자 대입
        graph[x][y] = i

        # 다음 좌표로 이동
        nx = x
        ny = y + 1

        # y좌표가 n 이상일 경우 (= 해당 줄 탐색이 끝난 경우)
        if ny >= N:
            # 해당 줄 가로 방향 숫자 검증, 아닐 경우 좌표 초기화 후 리턴
            if check(graph[x]) != left[x] or check(graph[x][::-1]) != right[x]:
                graph[x][y] = 0
                continue

            # 맞으면 좌표 갱신
            nx += 1
            ny = 0

        # 다음 좌표 재귀
        func(nx, ny)
        # 재귀 종료 후 해당 좌표 초기화
        graph[x][y] = 0


func(0, 0)