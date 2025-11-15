max_info = input()
num_of_item = int(max_info.split(" ")[0])
max_w = int(max_info.split(" ")[1])
item_info = []
i = 0
while i < num_of_item:
    new = input()
    new_data = new.split(" ")
    item_info.append([int(new_data[1])/int(new_data[0]),int(new_data[0]),int(new_data[1])])
    i += 1

item_info.sort(reverse=True)

bag = []

def value(bag):
    ans = 0
    for p in bag:
        ans+=p[2]
    return ans

def weight(bag):
    ans = 0
    for p in bag:
        ans += p[1]
    return ans

val = 0
start = 0

while start < num_of_item:
    if item_info[start][1] > max_w:
        start += 1
        continue
    bag.append(item_info[start])
    ind = 0
    while ind < num_of_item:
        if ind == start:
            ind += 1
            continue
        if weight(bag) + item_info[ind][1] <= max_w:
            bag.append(item_info[ind])
        else:
            pass
        ind += 1
    if val < value(bag):
        val = value(bag)
    start += 1
    print(bag)
    bag = []

print(val)