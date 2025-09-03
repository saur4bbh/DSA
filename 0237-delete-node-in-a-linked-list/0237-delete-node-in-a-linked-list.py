class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        i = node
        while i.next:
            i.val = i.next.val
            if i.next.next is None:
                i.next = None
                break
            i = i.next
        