n = int(input())

result = []
def hanoi(n, now, goal):
    if n > 1:
        goal = 6 - now - goal
        hanoi(n - 1, now, goal)
        goal = 6 - now - goal
        result.append((now, goal))
        now = 6 - now - goal
        hanoi(n - 1, now, goal)

    elif n == 1:
        result.append((now, goal))

hanoi(n, 1, 3)
print(pow(2, n) - 1)
for item in result:
    x, y = item
    print(x, y)