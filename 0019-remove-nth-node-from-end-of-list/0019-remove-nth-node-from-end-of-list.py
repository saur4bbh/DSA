# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        j = head

        for _ in range(n):
            j = j.next
        
        if not j:
            head = i.next
            return head

        while j.next:
            i = i.next
            j = j.next
        
        i.next = i.next.next
        return head