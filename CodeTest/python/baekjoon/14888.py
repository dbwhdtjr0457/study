n = int(input())
arr = list(map(int, input().split()))
op_arr = list(map(int, input().split()))

result = [float('-inf'), float('inf')]
curr = arr[0]
def operate(arr, op_arr, result, curr, i):
    if i == len(arr):
        result[0] = max(result[0], curr)
        result[1] = min(result[1], curr)
    else:
        if op_arr[0] > 0:
            temp = curr + arr[i]
            op_arr[0] -= 1
            operate(arr, op_arr, result, temp, i + 1)
            op_arr[0] += 1
        if op_arr[1] > 0:
            temp = curr - arr[i]
            op_arr[1] -= 1
            operate(arr, op_arr, result, temp, i + 1)
            op_arr[1] += 1
        if op_arr[2] > 0:
            temp = curr * arr[i]
            op_arr[2] -= 1
            operate(arr, op_arr, result, temp, i + 1)
            op_arr[2] += 1
        if op_arr[3] > 0:
            if curr < 0:
                temp = -((curr * (-1)) // arr[i])
            else:
                temp = curr // arr[i]
            op_arr[3] -= 1
            operate(arr, op_arr, result, temp, i + 1)
            op_arr[3] += 1
            

operate(arr, op_arr, result, curr, 1)

print(result[0])
print(result[1])