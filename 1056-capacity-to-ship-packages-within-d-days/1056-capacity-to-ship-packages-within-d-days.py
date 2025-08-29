class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def currentday(val):
            ans = 1
            carry = 0
            for w in weights:
                if carry + w > val:
                    carry = 0
                    ans += 1
                carry += w
            return ans

        l, r = max(weights), sum(weights) 

        while l <= r:
            mid = (l + r) // 2
            if currentday(mid) > days:
                l = mid + 1
            else:
                r = mid - 1

        return l

            


                