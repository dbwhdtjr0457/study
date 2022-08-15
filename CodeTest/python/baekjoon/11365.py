while True:
    data = input()
    if data == "END":
        break
    for i in range(len(data) - 1, -1, -1):
        print(data[i], end='')
    print()