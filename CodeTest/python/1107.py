import sys
input = sys.stdin.readline

goal = int(input()) # 목표
n = int(input()) # 고장 버튼 개수
if n == 0: # 고장 개수 없으면 다음 인풋 없음
    exclude = []
else: 
    exclude = list(map(int, input().split()))

button = [True] * 10 # 고장난 버튼 리스트

for item in exclude: 
    button[item] = False

# 1. 숫자 입력 안 하고 +, -만 누름
default = 100 # 기본 숫자

result1 = abs(goal - default)

# 2. 새로 숫자 입력 후 +, - 누름
current = "" 

ok1 = ok2 = goal # ok1, ok2에 목표 값 할당 후 각각 +1, -1 반복하면서 가능한 숫자 탐색

result2Solved = False

for item in button: # 만약 버튼이 다 불구일 경우 result2 구하는 것 배제
    if item == True:
        result2Solved = True

if result2Solved == True:
    result2_1 = result2_2 = None
    if exclude == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        result2_1 = 10000000000
    while result2_1 is None or result2_2 is None:
        rightInput1 = rightInput2 = True
        ok1_list = list(map(int, str(ok1)))
        ok2_list = list(map(int, str(ok2)))
        for num in ok1_list:
            if button[num] == False:
                rightInput1 = False
                break
        for num in ok2_list:
            if button[num] == False:
                rightInput2 = False
                break

        if rightInput1 == True and result2_1 is None:
            current = ok1
            result2_1 = len(str(ok1)) + abs(goal - int(current))
            
        if rightInput2 == True and result2_2 is None:
            current = ok2
            result2_2 = len(str(ok2)) + abs(goal - int(current))
        
        ok1 += 1
        if ok2 > 0:
            ok2 -= 1




if result2Solved == True:
    result2 = min([result2_1, result2_2])
    print(min([result1, result2]))
else:
    print(result1)