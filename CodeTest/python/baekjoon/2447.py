n = int(input())

defaultData = []
result = []

def solution(n):
    global defaultData, result
    if n == 3:
        result.append("***")
        result.append("* *")
        result.append("***")
        defaultData = result[:]
    else:
        solution(n // 3)
        for i in range(n // 3):
            result[i] = result[i] * 3
        for i in range(n // 3):            
            result.append(defaultData[i] + ' ' * (n // 3) + defaultData[i])
        for i in range(n // 3):
            result.append(result[i])
    defaultData = result[:]

solution(n)

for row in result:
    print(row)