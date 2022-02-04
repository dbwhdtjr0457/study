import math

power, sleep, goal = map(int, input().split())

dayHeight = power - sleep

ableHeight = goal - power

print(math.ceil(ableHeight / dayHeight) + 1)