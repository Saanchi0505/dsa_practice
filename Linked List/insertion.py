class Node:
    def __init__(self,data):
        self.data =data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next!=None:
            temp =temp.next
        temp.next=new_node
    
    def deletion_from_begining(self):
        if self.head is None:
            print('List is Empty')
            return
        self.head = self.head.next

    def display(self):
        temp = self.head
        while temp!=None:
            print(temp.data,end='->')
            temp = temp.next
        print('None')

l1 = LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.display()
l1.deletion_from_begining()
l1.display()