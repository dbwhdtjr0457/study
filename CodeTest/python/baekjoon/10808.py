arr = [0] * 26
data = input()

for i in range(len(data)):
    arr[ord(data[i]) - 97] += 1

print(*arr)