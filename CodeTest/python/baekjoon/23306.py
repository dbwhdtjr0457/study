import sys


n = int(input())

print("? 1")
response1 = int(input())
print("? " + str(n))
response2 = int(input())

if response1 == 1 and response2 == 0:
    print("! -1")
elif response1 == 0 and response2 == 1:
    print("! 1")
else:
    print("! 0")
