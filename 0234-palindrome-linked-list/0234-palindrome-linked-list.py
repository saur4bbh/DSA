# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def rev(idx):
            i = head
            while idx != 0:
                i = i.next
                idx -= 1

            prev = i
            i = i.next
            while i:
                after = i.next
                i.next = prev
                prev = i
                i = after
            return prev

        i = head
        count = 1
        while i.next:
            i = i.next
            count += 1

        mid = count // 2

        i = head
        j = rev(mid)

        while mid != 0:
            mid -= 1
            if i.val != j.val:
                return False
            i = i.next
            j = j.next

        return True



