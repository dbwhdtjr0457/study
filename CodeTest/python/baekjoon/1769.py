n = int(input())

count = 0
while n >= 10:
    count += 1
    n = sum(map(int, str(n)))
print(count)
if n % 3:
    print("NO")
else:
    print("YES")