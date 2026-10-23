"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        ptr = dummy
        head1 = head
        hashmap = {None: None}

        while head1:
            ptr.next = Node(head1.val)
            ptr = ptr.next
            hashmap[head1] = ptr
            head1 = head1.next

        head2 = head
        ptr2 = dummy.next
        while head2:
            ptr2.random = hashmap[head2.random]
            head2 = head2.next
            ptr2 = ptr2.next

        return dummy.next
