class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        seen = set(jewels)
        
        for s in stones:
            if s in seen:
                ans += 1

        return ans