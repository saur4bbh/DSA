class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        x = n
        ans = 0
        while x != 0:
            ans += x%10
            x //= 10
        
        return ans