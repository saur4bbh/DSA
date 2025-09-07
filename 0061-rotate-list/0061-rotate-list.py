# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k or not head.next:
            return head
        
        total = 1
        j = head
        while j.next:
            j = j.next
            total += 1

        k = k % total
        val = total - k
        if k == 0 or val == 0:
            return head
        i = head
        for _ in range(val-1):
            i = i.next
        
        ans = i.next
        i.next = None
        j.next = head

        return ans


        
