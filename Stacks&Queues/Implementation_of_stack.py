class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty():
            return "Stack Not defined"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) ==0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()

s.pop()
s.pop()
s.display()
print(s.peek())
print(s.size())
print(s.is_empty())