# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1 = headA
        temp2 = headB

        while temp1!=temp2:
            if temp1 is None:
                temp1 = headB
            else:
                temp1 = temp1.next 
            if temp2 is None:
                temp2 = headA
            else:
                temp2 = temp2.next
        return temp1
        