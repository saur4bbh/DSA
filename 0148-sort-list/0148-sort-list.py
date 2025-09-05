# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,l1,l2):
            dum = ListNode(0)
            tail = dum

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            tail.next = l1 or l2
            return dum.next

    def sortList(self, low: Optional[ListNode]) -> Optional[ListNode]:

        if not low or not low.next:
            return low
        mid = low
        h = low.next
        while h and h.next:
            mid = mid.next
            h = h.next.next

        mid2 = mid.next
        mid.next = None

        x = self.sortList(low)
        y = self.sortList(mid2)
        return self.merge(x,y)

            
