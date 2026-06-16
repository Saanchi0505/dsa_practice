class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next=newnode
        newnode.prev =temp
    def reverse(self):
        if self.head is None:
            return
        temp=None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev=current.next
            current.next=temp
            current=current.prev
        self.head = temp.prev
    def display(self):
        if self.head is None:
            print('Empty')
            return
        temp = self.head
        while temp is not None:
            print(temp.data,end='->')
            temp = temp.next
        print('None')

dll = DoublyLL()
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)
dll.display()
dll.reverse()
dll.display()