"""Starting with doubly linked list"""
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
    def insert_at_beg(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        newnode.next = self.head
        self.head.prev = newnode
        self.head=newnode

    def insert_at_idx(self,data,idx):
        newnode = Node(data)
        if idx==0:
            self.insert_at_beg()
            return
        temp = self.head
        for i in range(idx-1):
            temp=temp.next
        newnode.next = temp.next
        newnode.prev=temp
        temp.next=newnode

    def delete_at_begin(self):
        if self.head is None:
            print("List is Empty")
            return
        self.head = self.head.next
        self.head.prev = None
    def delete_at_end(self):
        temp =self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next.prev= None
        temp.next=None

    def delete_at_idx(self,idx):
        temp = self.head
        for i in range(idx - 1):
            temp = temp.next
        node_to_delete = temp.next
        temp.next = node_to_delete.next
        if node_to_delete.next is not None:
            node_to_delete.next.prev = temp

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
dll.insert_at_beg(4)
dll.display()
dll.insert_at_idx(5,2)
dll.display()
dll.delete_at_begin()
dll.display()
dll.delete_at_end()
dll.display()
dll.delete_at_idx(1)
dll.display()
