arr = []
while True:
    data = input()
    if data == '0':
        break
    arr.append(data)

for item in arr:
    i = 0
    while 0 <= i <= len(item) - 1 and item[i] == item[len(item) - i - 1] and i <= len(item) - i - 1:
        i += 1
    if i > len(item) - i - 1:
        print("yes")
    else:
        print("no")
