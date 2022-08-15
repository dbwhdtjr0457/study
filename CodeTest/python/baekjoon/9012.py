n = int(input())

for _ in range(n):
    data = input()
    temp = 0
    flag = True
    for i in range(len(data)):
        if data[i] == '(':
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            flag = False
            break
    if flag and temp == 0:
        print("YES")
    else:
        print("NO")