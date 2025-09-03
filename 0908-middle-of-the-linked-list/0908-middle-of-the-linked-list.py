# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        move = 0
        mid = head
        i = head
        while i.next:
            i = i.next
            if move % 2 == 1:
                mid = mid.next
            move += 1
        return mid.next if move%2 == 1 else mid