# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB

        while a.next and b.next:
            a = a.next
            b = b.next

        i = headA if a.next else headB
        j = headA if i == headB else headB

        while a.next:
            a = a.next
            i = i.next
        while b.next:
            b = b.next
            i = i.next
        
        while i and j:
            if i == j:
                return i
            i = i.next
            j = j.next
        