class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen = {}

        for j in jewels:
            seen[j] = 0
        
        for s in stones:
            if s in seen:
                seen[s] += 1
            
        return sum(seen.values())