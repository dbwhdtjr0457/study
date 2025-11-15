word = input()

alphaList = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

checkWord = ""

result = 0

wordIdx = 0

for i in range(len(word)):
    if wordIdx > i:
        continue
    for alpha in alphaList:
        if word[i:i + len(alpha)] == alpha:
            wordIdx = i + len(alpha)
            break
    result += 1

print(result)