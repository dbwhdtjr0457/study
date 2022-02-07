import sys


n, k = map(int, sys.stdin.readline().split())

alphaList = sys.stdin.readline().split()

alphaList.sort()

vowels = ("a", "e", "i", "o", "u")


def solve(password, index):
    if len(password) < n:
        for i in range(index, k):
            nextPassword = password + alphaList[i]
            solve(nextPassword, i + 1)
    elif len(password) == n:
        consonentNum = 0
        vowelNum = 0

        for alphabet in password:
            if alphabet in vowels:
                vowelNum += 1
            else:
                consonentNum += 1

        if consonentNum >= 2 and vowelNum >= 1:
            print(password)


solve("", 0)
