class Node:
    def __init__(self,data):
        self.data =data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next!=None:
            temp =temp.next
        temp.next=new_node

    def insert_at_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next= self.head
        self.head= new_node
    
    def insert_at_idx(self,data,idx):
        if idx==0:
            self.insert_at_beg()
        newnode = Node(data)
        temp = self.head
        for i in range(idx-1):
            if temp is None or temp.next is None:
                print('invalid idx')
                return
            temp = temp.next
        newnode.next = temp.next
        temp.next=newnode

    
    def deletion_from_begining(self):
        if self.head is None:
            print('List is Empty')
            return
        self.head = self.head.next

    def delete_at_idx(self,idx):
        if idx==0:
            self.deletion_from_begining()
            return
        temp = self.head
        for i in range(idx-1):
            if temp is None or temp.next is None:
                print('index out of range')
            temp= temp.next
        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp!=None:
            print(temp.data,end='->')
            temp = temp.next
        print('None')




l1 = LinkedList()
l1.insert_at_end(1)
l1.insert_at_end(2)
l1.insert_at_end(3)
l1.display()
l1.deletion_from_begining()
l1.display()
l1.insert_at_end(4)
l1.insert_at_end(5)
l1.display()
l1.delete_at_idx(2)
l1.insert_at_beg(6)
l1.insert_at_idx(7,2)
l1.display()
