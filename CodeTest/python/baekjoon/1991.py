n = int(input())

tree = {}

for i in range(n):
    parent, child_1, child_2 = input().split()
    tree[parent] = [child_1, child_2]

def preorder(item):
    if (item != "."):
        print(item, end="")
        preorder(tree[item][0])
        preorder(tree[item][1])

def inorder(item):
    if (item != "."):
        inorder(tree[item][0])
        print(item, end="")
        inorder(tree[item][1])

def postorder(item):
    if (item != "."):
        postorder(tree[item][0])
        postorder(tree[item][1])
        print(item, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")