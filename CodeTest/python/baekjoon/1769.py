"""
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
    """

def check(num_list, cnt):
    if len(num_list) == 1:
        return int(num_list[0]), cnt
    else:
        summary = list(str(sum(list(map(int, num_list)))))
        return check(summary, cnt + 1)


N = list(input())
cnt = 0

N, cnt = check(N, cnt)
print(cnt)
if N % 3 == 0:
    print("YES")
else:
    print("NO")
