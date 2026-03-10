class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        ans = 0
        while y > 0:
            ans *= 10
            ans += y%10
            y //= 10
        if -2**31 <= ans <= 2**31 - 1:
            return ans if x>=0 else -ans
        else:
            return 0