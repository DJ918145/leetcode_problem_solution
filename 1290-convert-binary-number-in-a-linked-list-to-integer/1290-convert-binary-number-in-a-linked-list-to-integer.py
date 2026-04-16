# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        binary = ""
        while head!= None:
            binary += str(head.val)
            head = head.next
        print(binary)
        return int(binary, 2)