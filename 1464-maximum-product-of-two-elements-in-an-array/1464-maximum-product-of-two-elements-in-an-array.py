class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x = y = 0
        for i in nums:
            if i >= x:
                y = max(x, y)
                x = i
            elif i > y:
                y = i

        return (x-1) * (y-1)