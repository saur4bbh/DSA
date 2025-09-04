# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        prev = head
        end = head.next
        while end.next and end.next.next:
            end = end.next.next
            prev = prev.next

        prev.next = prev.next.next
        return head
