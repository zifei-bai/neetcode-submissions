# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        carry = 0
        while l1 or l2:
            if not l1:
                adds = l2.val + carry
            elif not l2:
                adds = l1.val + carry
            else:
                adds = l1.val + l2.val + carry

            if adds >= 10:
                adds -= 10
                carry = 1
            else:
                carry = 0
            
            ptr.next = ListNode(adds)
            ptr = ptr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry == 1:
            ptr.next = ListNode(carry)

        return dummy.next
        
