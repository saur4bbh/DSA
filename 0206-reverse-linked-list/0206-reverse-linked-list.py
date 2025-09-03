# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        i = head.next
        prev = head
        head.next = None

        while i:
            after = i.next
            i.next = prev
            prev = i
            i = after

        return prev

            
