class Stack:
    def __init__(self):
        self.stack = []
        
    def lenght(self):
        return len(self.stack)
    
    # insert krega 
    def push(self, value):
        self.stack.insert(0, value)
        
    # only stack ko dekhne ke liye
    def peek(self):
        if(self.stack) == 0:
            raise Exception("Stack khaali hai lwde")     
        
        else:
            return self.stack[0]
        
    # stack ke top element ko dlt krne kai liye
    def pop(self):
        if(self.stack == 0):
            raise Exception("Stack khali hai")
        
        else:
            return self.stack.pop(0)
        
    
obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)

print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())