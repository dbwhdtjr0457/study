arr = list(map(int, input().split()))

num1 = arr[0]
state = ''
for i in range(1, len(arr)):
    num2 = arr[i]
    if num1 < num2:
        if state == '':
            state = "ascending"
        elif state == "descending":
            state = "mixed"

    elif num1 > num2:
        if state == '':
            state = "descending"
        elif state == "ascending":
            state = "mixed"
    
    num1 = num2

print(state)