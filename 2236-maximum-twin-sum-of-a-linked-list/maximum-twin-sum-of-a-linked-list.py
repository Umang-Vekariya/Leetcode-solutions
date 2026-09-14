# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        slow = head
        fast = head
        curr = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next_slow = slow.next
            slow.next = prev
            prev = slow
            slow = next_slow
        s = 0
        while prev:
            s = max(s, curr.val + prev.val)
            curr = curr.next
            prev = prev.next
        
        return s