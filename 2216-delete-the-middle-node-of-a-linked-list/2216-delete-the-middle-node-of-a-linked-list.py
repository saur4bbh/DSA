# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        end = head
        while end and end.next:
            end = end.next.next
            if end and end.next:
                start = start.next
        
        if start is end or start.next is end:
            return head.next
        
        start.next = start.next.next
        return head
