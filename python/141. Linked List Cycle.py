# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = head.next
        slow = head
        while fast != slow:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
