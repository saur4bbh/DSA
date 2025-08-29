class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n: return -1
        l, r = min(bloomDay), max(bloomDay)

        def bloom(days):
            ans = 0
            i = 0
            while i < n:
                t = 0
                while i<n and bloomDay[i] - days <= 0:
                    i += 1
                    t += 1
                ans += t//k
                i += 1
            return ans

        while l <= r:
            mid = (l + r) // 2
            
            if bloom(mid) >= m:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
            
