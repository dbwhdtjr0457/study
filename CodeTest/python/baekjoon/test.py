# Enter your code here. Read input from STDIN. Print output to STDOUT
wormholeNum, N = map(int, input().split())

universe = {}

starList = []

for _ in range(wormholeNum):
    star1, star2 = input().split()
    
    if star1 not in universe:
        starList.append(star1)
        universe[star1] = [[star2], False]
    else:
        universe[star1][0].append(star2)
        
    if star2 not in universe:
        starList.append(star2)
        universe[star2] = [[star1], False]
    else:
        universe[star2][0].append(star1)
        
def bfs(universe, star, count):
    universe[star][1] = True
    count += 1
    for otherStar in universe[star][0]:
        if not universe[otherStar][1]:
            bfs(universe, otherStar, count)

result = 0        

for star in starList:
    if not universe[star][1]:
        count = 0
        bfs(universe, star, count)
        print(count)
        if count <= N:
            result += count
            
print(result)

