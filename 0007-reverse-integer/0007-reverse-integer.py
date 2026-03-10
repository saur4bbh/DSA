class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        ans = 0

        while y > 0:
            ans = (ans * 10) + (y % 10)
            y //= 10
            
        if ans > 2**31 - 1:
            return 0

        return ans if x>=0 else -ans