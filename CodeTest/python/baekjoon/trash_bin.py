n = int(input())

result = ''

for i in range(n):
    string = bin(i)
    result += string[2:]

print(result)
