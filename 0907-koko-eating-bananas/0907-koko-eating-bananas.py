class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eat(k):
            t = 0
            for pile in piles:
                t += (pile + k - 1) // k
                if t>h: 
                    return -1
            return t
                
        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r) // 2
            if eat(mid) == -1:
                l = mid + 1
            else:
                r = mid - 1

        return l


        