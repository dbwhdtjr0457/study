from collections import Counter

common = Counter(list(map(int, input().split()))).most_common()
print(10000 + 1000 * common[0][0]) if common[0][1] == 3 else print(1000 + 100 * common[0][0]) if common[0][1] == 2 else print(100 * sorted(common, key=lambda x:x[0], reverse=True)[0][0])