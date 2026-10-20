class Node:
    def __init__(self,info, prev = None, next = None):
        self.prev = prev
        self.data = info
        self.next = next
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beggning(self,data):
        new_node = Node(10)
        
        if self.head == None:
            self.head = new_node
            return
        
        # Remember- the order: connect the new node to the old head, 
        # connect the old head back to the new node, and then update the head.
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current
        
        
        
    def display_list(self):
            current = self.head
            while current is not None:
                print(current.data, end=" <--> ")
                current = current.next
                
            print("None")
        

Dll = DoublyLinkedList()

Dll.insert_at_beggning(10)

Dll.display_list()

Dll.insert_at_end(20)
Dll.display_list()
