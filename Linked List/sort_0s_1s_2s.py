class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
	
class Solution:
    def segregate(self, head):
        #code here
        temp  = head
        zero_head = Node(-1)
        two_head = Node(-1)
        one_head = Node(-1)
        zero = zero_head
        one = one_head
        two=two_head
        
        while temp is not None:
            if temp.data==0:
                zero.next=temp
                zero = zero.next
            elif temp.data==1:
                one.next = temp
                one =one.next
            else:
                two.next=temp
                two=two.next
            temp = temp.next
            
        zero.next = one_head.next if one_head.next else two_head.next
        one.next = two_head.next
        two.next = None

        return zero_head.next if zero_head.next else (
               one_head.next if one_head.next else two_head.next)
    