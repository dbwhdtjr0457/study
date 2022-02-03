from collections import deque


queue = deque()

queue.append(1)
queue.append(2)

print(queue.index(1))
print(queue.index(3))