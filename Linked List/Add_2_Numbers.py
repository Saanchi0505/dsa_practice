
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy  = ListNode(-1)
        current = dummy
        carry = 0
        while l1 is not None or l2 is not None:
            sum = carry
            if l1:
                sum += l1.val
            if l2:
                sum+= l2.val
            newnode = ListNode(sum%10)
            carry = sum//10
            current.next=newnode
            current = current.next
            if l1:
                l1=l1.next
            if l2:
                l2 = l2.next
        if carry:
            newnode = ListNode(carry)
            current.next = newnode
        
        return dummy.next