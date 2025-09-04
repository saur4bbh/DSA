# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
            
        prev = ListNode(0, head)
        end = head
        while end and end.next:
            end = end.next.next
            prev = prev.next

        prev.next = prev.next.next
        return head
