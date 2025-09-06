# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = l1
        carry = 0

        while l1 and l2:
            l1.val += l2.val + carry
            if l1.val >= 10:
                l1.val = l1.val % 10
                carry = 1 
            else:
                carry = 0
            if not l1.next and not l2.next and carry == 1:
                l1.next = ListNode(1,None)
                return i
            if not l1.next:
                l1.next = l2.next
                l1 = l1.next
                break
            l1 = l1.next
            l2 = l2.next
        

        while l1:
            l1.val += carry
            if l1.val >= 10:
                l1.val = l1.val % 10
                carry = 1 
            else:
                carry = 0
            if not l1.next and carry == 1:
                l1.next = ListNode(1,None)
                break
            l1 = l1.next
            
        return i

