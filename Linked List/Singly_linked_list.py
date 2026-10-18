# creating Node
class Node:
    def __init__(self, info,next = None):
        self.data = info
        self.next = next
        
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)



node1.next = node2
node2.next = node3

head = node1

current = head
while current != None:
    print(current.data, end= " -> ")
    current = current.next
print("None")
    