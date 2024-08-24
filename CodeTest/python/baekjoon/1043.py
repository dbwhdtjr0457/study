result = 0

N, M = map(int, input().split())
truthList = list(map(int, input().split()))
# 진실 아는 사람 수
truthCount = truthList[0]
# 진실 아는 사람 리스트
truthList = truthList[1:]

# 파티 이차원 리스트
partyMatrix = []

# 사람 관계 이차원 리스트
relMatrix = [set() for _ in range(N + 1)]

for i in range(M):
    temp = list(map(int, input().split()))
    partyCount = temp[0]
    partySet = set(temp[1:])
    partyMatrix.append(partySet)
    partyList = list(partySet)
    
    # 관계있는 사람 연결
    for j in range(len(partyList) - 1):
        for k in range(j + 1, len(partyList)):
            x, y = partyList[j], partyList[k]
            relMatrix[x].add(y)
            relMatrix[y].add(x)


# 아는 사람들이 포함된 파티에 있는 다른 사람들을 truthList에 포함
newTruthSet = set()

def dfs(person):
    newTruthSet.add(person)
    for others in list(relMatrix[person]):
        if (others not in newTruthSet):
            dfs(others)

for person in truthList:
    dfs(person)

for party in partyMatrix:
    ok = True
    for knower in newTruthSet:
        if knower in party:
            ok = False
    
    result += ok

print(result)