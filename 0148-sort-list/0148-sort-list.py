# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1,l2):
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

        def divide(low):
            if not low or not low.next:
                return low
            mid = low
            h = low.next
            while h and h.next:
                mid = mid.next
                h = h.next.next

            mid2 = mid.next
            mid.next = None

            x = divide(low)
            y = divide(mid2)
            return merge(x,y)

        return divide(head)

            
