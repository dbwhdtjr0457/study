testList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def insertionSort(testList):
    for i in range(1, len(testList)):
        for j in range(i, 0, -1):
            if testList[j] < testList[j - 1]:
                testList[j], testList[j - 1] = testList[j - 1], testList[j]
            else:
                break
        


insertionSort(testList)

print(testList)