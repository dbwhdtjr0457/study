data = input()

alphaList = [-1] * 26

for i in range(len(data)):
    num = ord(data[i])
    index = num - 97
    
    if alphaList[index] == -1:
        alphaList[index] = i
    
for i in alphaList:
    print(i, end = ' ')