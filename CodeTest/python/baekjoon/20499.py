a = input()
arr = list(map(int, a.split('/')))

if arr[0] + arr[2] < arr[1] or arr[1] == 0:
    print("hasu")
else:
    print("gosu")