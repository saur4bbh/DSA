# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        i = head
        while i:
            ans.append(i.val)
            i = i.next

        ans.sort(reverse = True)
        i = head
        while i:
            i.val = ans.pop()
            i = i.next

        return head