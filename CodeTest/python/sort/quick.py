testList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    return quickSort(lesser_arr) + equal_arr + quickSort(greater_arr)


testList = quickSort(testList)

print(testList)