import sys

n = int(input())

tempArr = []
resultArr = []
num = 1
flag = True
for i in range(n):
    k = int(sys.stdin.readline().strip())
    if k >= num:
        while k != num:
            tempArr.append(num)
            num += 1
            resultArr.append('+')
        num += 1
        resultArr.append('+')
        resultArr.append('-')
    elif k == tempArr[-1]:
        tempArr.pop()
        resultArr.append('-')
    else:
        flag = False

if flag:
    for item in resultArr:
        print(item)
else:
    print("NO")