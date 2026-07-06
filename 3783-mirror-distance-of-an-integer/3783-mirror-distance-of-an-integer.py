class Solution:
    def mirrorDistance(self, n: int) -> int:
        def rev(x):
            r = 0
            while x != 0:
                r = (r * 10) + (x % 10)
                x = x // 10
            return r

        return abs(n - rev(n))