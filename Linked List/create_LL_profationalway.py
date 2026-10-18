class Node:
    def __init__(self, info, next= None):
        self.data = info
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
     
    # adding nodes in last
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        
        while current.next is not None:
            current = current.next
            
        current.next = new_node
        
    # insert at the begning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        current = self.head
        
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
            
        print("None")
        
    
ll = LinkedList()

ll.append(20)
ll.append(40)
ll.append(50)

ll.display()

ll.prepend(10)
ll.display()