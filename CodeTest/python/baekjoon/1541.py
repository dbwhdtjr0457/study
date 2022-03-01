s = input()
startIndex = 0
numList = s.split('-')

for i in range(len(numList)):
    subList = map(int, numList[i].split('+'))
    numList[i] = sum(subList)

for i in range(1, len(numList)):
    numList[0] -= numList[i]

print(numList[0])
