while True:
    inputstr = input()

    if inputstr == "#":
        break;

    count = 0
    count += inputstr.count('a')
    count += inputstr.count('e')
    count += inputstr.count('i')
    count += inputstr.count('o')
    count += inputstr.count('u')
    count += inputstr.count('A')
    count += inputstr.count('E')
    count += inputstr.count('I')
    count += inputstr.count('O')
    count += inputstr.count('U')
    
    print(count)