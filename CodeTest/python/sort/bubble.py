testList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def bubbleSort(testList):
    for i in range(len(testList) - 1, 0, -1):
        for j in range(0, i):
            if (testList[j] > testList[j + 1]):
                testList[j], testList[j + 1] = testList[j + 1], testList[j]
            

bubbleSort(testList)

print(testList)