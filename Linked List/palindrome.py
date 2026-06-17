# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def find_mid(self,head):
        slow = head
        fast=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
    def reverse(self,head):
        temp=head
        prev=None
        while temp is not None:
            front = temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        first =head
        mid = self.find_mid(head)
        new_head = self.reverse(mid.next)
        second=new_head
        while second is not None :
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True
