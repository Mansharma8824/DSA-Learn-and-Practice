class Queue:
    def __init__(self):
        self.item = []
        
    def isEmpty(self):
        return len(self.item) == 0

    def enqueue(self, value):
        self.item.append(value)
        print(f"Inserted {value}")
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return None
        removed = self.item.pop(0)
        print(f"Removed {removed}")
        
    def peak(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.item[0]
        
    def display_queue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else :
            print("Fron ->", end=" ")
        
        for item in self.item:
            print(item, end=" ")
            
        print("<- End")


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.peak())
q.display_queue()

q.dequeue()
print(q.peak())
q.display_queue()

q.dequeue()
print(q.peak())
q.display_queue()



