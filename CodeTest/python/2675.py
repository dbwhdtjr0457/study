n = int(input())

for _ in range(n):
    num, string = input().split()
    num = int(num)

    for i in string:
        print(i * num, end = '')
    
    print()