# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        index = 0
        while slow and fast and fast.next:
            if index != 0 and slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
            index += 1
        return False