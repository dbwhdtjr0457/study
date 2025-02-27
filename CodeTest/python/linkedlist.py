class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        if self.head is None:
            return "no data"
        res = "head"
        node = self.head
        while node is not None:
            res += " -> " + str(node.data)
            node = node.next
        return res
    
    def appendleft(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)
        self.length += 1

    def popleft(self):
        if self.head == None:
            return None
        else:
            node = self.head
            self.head = node.next
            self.length -= 1
            return node.data

my_list = LinkedList()
for i in range(4):
    my_list.append(str(i))
print(my_list)
