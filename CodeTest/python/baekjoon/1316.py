n = int(input())

result = n

for _ in range(n):
    word = input()
    alphaDict = set()
    currAlpha = None

    for i in range(len(word)):
        if word[i] == currAlpha:
            continue
        if word[i] not in alphaDict:
            alphaDict.add(currAlpha)
            currAlpha = word[i]
        else:
            result -= 1
            break

print(result)
