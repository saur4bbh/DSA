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
        i = head
        while i:
            copy = Node(i.val)
            temp = i.next
            i.next = copy
            copy.next = temp
            i = i.next.next

        i = head
        while i:
            if i.random:
                i.next.random = i.random.next
            else:
                i.next.random = None
            i = i.next.next
        
        dum = Node(0)
        i = dum
        j = head
        while j:
            i.next = j.next
            j.next = j.next.next
            i = i.next
            j = j.next
        
        return dum.next