n, k = map(int, input().split())

notHeard = set()

for _ in range(n):
    notHeard.add(input())

notHeardAndSeen = []

for _ in range(k):
    newName = input()
    if newName in notHeard:
        notHeardAndSeen.append(newName)

notHeardAndSeen.sort()

print(len(notHeardAndSeen))
for name in notHeardAndSeen:
    print(name)
