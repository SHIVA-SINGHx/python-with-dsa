# 1. QUEUE

# class Queue:
#     def __init__(self):
#         self.items = []
        
#     def isEmpty(self):
#         return len(self.items) == 0
    
#     def insert(self, value):
#         self.items.append(value)
    
#     def delete(self):
#         if(self.isEmpty()):
#             print("Queue is empty")
#         else:
#             return self.items.pop(0)
        
        
# q = Queue()
# q.insert(10)
# q.insert(20)
# q.insert(30)


# print(q.delete())
# print(q.delete())
# print(q.delete())
# q.delete()

####################################################
# 2. DOUBLE ENDED QUEUE (DEQUEUE)

# class Deque:
#     def __init__(self):
#         self.items = []
        
#     def isEmpty(self):
#         return len(self.items) == 0
           
#     def insertAtEnd(self, value):
#         self.items.append(value)
        
#     def deleteAtFront(self):
#         if(self.isEmpty()):
#             print("Queue is empty")
#         else:
#             return self.items.pop(0)
        
#     def insertAtFront(self, value):
#         self.items.insert(0, value)
        
#     def deleteAtEnd(self):
#         if(self.isEmpty()):
#             print("Queue is empty")
#         else:
#             return self.items.pop()
        
# dq = Deque()
# dq.insertAtEnd(10)
# dq.insertAtFront(20)
# dq.insertAtEnd(30)
# dq.insertAtEnd(40)
# dq.insertAtFront(50)

# print(dq.deleteAtEnd())
# print(dq.deleteAtEnd())
# print(dq.deleteAtFront())
# print(dq.deleteAtFront())
# print(dq.deleteAtEnd())

# dq.deleteAtEnd()
# dq.deleteAtFront()


################################################################

# 3. CIRCULAR QUEUE 

class CircularQueue:
    def __init__(self, size):
        self.size = size # jo user dega size like any int.
        self.items = [None]*size  # jitna size hoga utna size ka list ban jayga and sbme none fill ho jayga
        self.front = self.rear = - 1 
        
    # creation
    def enqueue(self, value):
        if((self.rear + 1  ) % self.size == self.front):
            print("Queue is full")
            
        elif self.front == -1 :
            self.front = self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1 ) % self.size
            self.items[self.rear]= value
    
    # deletion
    def dequeue(self):
        if(self.front == -1):
            print("Queue is empty")
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size
            
cq = CircularQueue(5)
cq.enqueue(10)        
cq.enqueue(20)        
cq.enqueue(30)        
cq.enqueue(40)
cq.enqueue(50)

cq.dequeue()

cq.enqueue(60)
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.dequeue()
    
    