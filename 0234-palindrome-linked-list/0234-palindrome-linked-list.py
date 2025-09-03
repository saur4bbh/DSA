# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            after = slow.next
            slow.next = prev
            prev = slow
            slow = after


        i = head
        j = prev

        while j:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next

        return True



