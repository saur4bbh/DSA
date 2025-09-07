# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def rev(start, endptr):
            newtail = start.next

            prev = endptr
            curr = start.next
            while curr != endptr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            start.next = prev
            return newtail
        

        dummy = ListNode(0,head)
        ini = dummy
        i = head
        cnt = 0

        while i:
            cnt += 1
            if cnt == k:
                right = i.next
                ini = rev(ini,right)
                i = right
                cnt = 0
            else:
                i = i.next

        return dummy.next
