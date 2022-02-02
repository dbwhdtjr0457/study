from pprint import pprint


newList =  [[0] * 10 for _ in range(10)]
for row in newList:
    print(row)

print("\n")
newList[1][1] = 1
for row in newList:
    print(row)