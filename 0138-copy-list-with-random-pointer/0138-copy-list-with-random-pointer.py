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
        mapp = {}

        i = dummy
        j = head
        while j:
            i.next = Node(j.val)
            i = i.next
            mapp[j] = i
            j = j.next

        mapp[j] = i.next
        
        i = dummy.next
        j = head
        while j:
            i.random = mapp[j.random]
            i = i.next
            j = j.next
        
        return dummy.next