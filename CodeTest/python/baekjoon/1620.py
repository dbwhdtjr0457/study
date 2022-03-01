n, m = map(int, input().split())

dogam = {}

for i in range(n):
    pokemon = input()
    dogam[i + 1] = pokemon
    dogam[pokemon] = i + 1

answerSheet = []
for _ in range(m):
    quiz = input()
    if 'A' <= quiz[0] <= 'Z':
        answerSheet.append(dogam[quiz])
    else:
        answerSheet.append(dogam[int(quiz)])

for item in answerSheet:
    print(item)
