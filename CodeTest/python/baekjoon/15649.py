from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
result = list(permutations(arr, m))
for items in result:
    print(*items, sep=' ')