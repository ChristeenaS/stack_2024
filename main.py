class Stack:
    
    def __init__(self):
        self.size =3
        self.stack = [None] * self.size
        self.top = -1
        
    def isFull(self):
        return self.top == self.size - 1
    
    def push(self,data):
        if self.isFull():
            print("Stack is full")
            return 
        self.top +=1
        self.stack[self.top] = data
        print("Pushed data : ",self.stack[self.top])
        
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        print("Removed data : ",self.stack[self.top])
        self.top = self.top -1
        
    def isEmpty(self):
        return self.top == -1
        
    def peep(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        return self.stack[self.top]
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("top element is:",stack.peep())
stack.push(4)
stack.pop()
stack.pop()
stack.pop()
stack.pop()




