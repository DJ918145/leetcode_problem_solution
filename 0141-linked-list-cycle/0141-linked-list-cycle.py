# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, abc):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not abc or not abc.next:
            return False
        curr = abc
        nex = abc.next
        while curr!=nex:
            if not nex or not nex.next:
                return False
            curr = curr.next
            nex = nex.next.next
        return True
        