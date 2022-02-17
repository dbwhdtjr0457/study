# 부분 성공
winLen = int(input()) * 2 + 1
dataLen = int(input())
data = input()

result = 0

for i in range(dataLen - winLen):
    ok = False
    if data[i] == 'I':
        ok = True
        for j in range(i + 1, i + winLen):
            if data[j] == data[j - 1]:
                ok = False
                break
    if ok == True:
        result += 1

print(result)
