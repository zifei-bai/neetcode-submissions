# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) <= 1:
            return None

        ps = [h for h in lists]
        while len(ps) > 1:
            mergedLists = []
            for i in range(0, len(ps), 2):
                dummy = ListNode()
                ptr = dummy
                ps1 = ps[i]
                ps2 = ps[i + 1] if (i + 1) < len(ps) else None
                while ps1 and ps2:
                    if ps1.val <= ps2.val:
                        ptr.next = ps1
                        ps1 = ps1.next
                    else:
                        ptr.next = ps2
                        ps2 = ps2.next
                    ptr = ptr.next
                if ps1:
                    ptr.next = ps1
                if ps2:
                    ptr.next = ps2
                mergedLists.append(dummy.next)
            ps =mergedLists
        return ps[0]