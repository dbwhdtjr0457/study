arr1 = [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
arr2 = [[3, 3, 3], [4, 4, 4], [5, 5, 100]]
print(list(map(list, zip(arr1, arr2))))