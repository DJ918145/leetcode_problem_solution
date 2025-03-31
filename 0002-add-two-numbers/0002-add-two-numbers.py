# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  # Dummy node to keep track of the head
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Sum of current digits and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry
            current.next = ListNode(total % 10)  # Create new node with the digit value
            
            # Move to the next elements
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next  # Return the next of dummy node, which is the result head

    # Helper function to create a linked list from a Python list
    def create_linked_list(lst):
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next