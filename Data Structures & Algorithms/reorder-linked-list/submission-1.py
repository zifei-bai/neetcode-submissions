# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        first_tail = None
        length = 0
        if not head.next:
            return
        while fast and fast.next:
            first_tail = slow
            slow = slow.next
            fast = fast.next.next
            length += 2
        first_tail.next = None
        prev = None
        while slow:
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex

        while head and prev:
            h_nex = head.next
            prev_nex = prev.next
            head.next = prev
            if h_nex:
                prev.next = h_nex
            
            head = h_nex
            if not head:
                print("yes")
                return
            prev = prev_nex


        return
