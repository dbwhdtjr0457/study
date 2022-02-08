n, k = map(int, input().split())

# 데이터를 딕셔너리로 저장
data = {}

for _ in range(n):
    id, password = input().split()
    data[id] = password

answer = []

for _ in range(k):
    answer.append(data[input()])

for item in answer:
    print(item)
