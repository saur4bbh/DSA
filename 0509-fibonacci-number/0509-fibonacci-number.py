class Solution:
    def fib(self, n: int) -> int:
        
        def rec(x):
            if x <= 1:
                return x
            ans = rec(x - 1) + rec(x - 2)
            return ans

        return rec(n)