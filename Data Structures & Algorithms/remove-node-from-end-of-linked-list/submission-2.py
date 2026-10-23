# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fix_head = head
        p = head
        prev_p = None
        count = 0
        while p:
            count += 1
            prev_p = p
            p = p.next

        if count == 1:
            return None

        scd_p = head
        prev = None
        num = 0
        while True:
            if (count - num) == n:
                if scd_p == fix_head:
                    # prev.next = None
                    return scd_p.next
                prev.next = scd_p.next
                break
            prev = scd_p
            scd_p = scd_p.next
            num += 1

        return head


        