n = int(input())

data = set()

for _ in range(n):
    inputList = input().split()
    if len(inputList) == 2:
        cmd, num = inputList[0], inputList[1]
        if cmd == "add" and num not in data:
            data.add(num)
        elif cmd == "remove" and num in data:
            data.remove(num)
        elif cmd == "check":
            if num in data:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if num in data:
                data.remove(num)
            else:
                data.add(num)
    else:
        cmd = inputList[0]
        if cmd == "all":
            data = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
                        '12', '13', '14', '15', '16', '17', '18', '19', '20'])
        elif cmd == "empty":
            data.clear()
