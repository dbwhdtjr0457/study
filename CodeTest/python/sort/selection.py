testList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def selectionSort(testList):
    for i in range(len(testList)):
        min_index = i
        for j in range(i + 1, len(testList)):
            if testList[min_index] > testList[j]:
                min_index = j
        testList[i], testList[min_index] = testList[min_index], testList[i]


selectionSort(testList)

print(testList)