data = input()
for item in data:
    if 'a' <= item <= 'z':
        print(chr(ord(item) - 32), end = '')
    else:
        print(chr(ord(item) + 32), end = '')