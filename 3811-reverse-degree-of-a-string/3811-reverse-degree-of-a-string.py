class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i,val in enumerate(s):
            ans += (i + 1) * (123 - ord(val))
        
        return ans