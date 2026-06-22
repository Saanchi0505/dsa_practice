from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
        
    def is_empty(self):
        return len(self.q)==0
    
    def enqueue(self,data):
        self.q.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return "Queue not defined"
        return self.q.popleft()
    
    def front(self):
        if self.is_empty():
            return None
        return self.q[0]
    def size(self):
        return len(self.q)
    def display(self):
        print(self.q)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()

q.dequeue()
q.dequeue()
q.dequeue()

q.display()

print(q.size())
print(q.front())
