import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rowEven = [True] * n
colEven = [True] * m

for i in range(n):
    row = input()
    for j, num in enumerate(row):
        if num == "1":
            rowEven[i] = not rowEven[i]
            colEven[j] = not colEven[j]

rowCountEven = rowEven.count(True)
rowCountOdd = len(rowEven) - rowCountEven
colCountEven = colEven.count(True)
colCountOdd = len(colEven) - colCountEven

rowMin = min(rowCountEven, rowCountOdd)
colMin = min(colCountEven, colCountOdd)

# result = 0

# if rowMin == 0:
#     if colMin == 0:
#         if rowEven[0] is False:
#             print(min(len(rowEven), len(colEven)))
#         else:
#             print(0)
#     else:
#         print(colCountOdd)
# else:
#     if colMin == 0:
#         print(rowCountOdd)
#     else:
#         result += rowMin
#         if rowMin % 2 == 0:
#             result += colCountOdd
#         else:
#             result += colCountEven
#         print(result)


result1 = 0
result2 = 0

result1 += min(rowCountEven, rowCountOdd)
if result1 % 2 == 0:
    result1 += colCountOdd
else:
    result1 += colCountEven

result2 += min(colCountEven, colCountOdd)
if result2 % 2 == 0:
    result2 += rowCountOdd
else:
    result2 += rowCountEven

print(min(result1, result2))
