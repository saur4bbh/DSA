# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def GCD(a, b):     
            while a != 0 and b != 0:
                if a >= b:
                    a %= b
                else:
                    b %= a
            return a if b == 0 else b
        
        i = head
        while i.next:
            gcd = GCD(i.val, i.next.val)
            dum = ListNode(gcd, i.next)
            i.next = dum
            i = i.next.next
        
        return head
