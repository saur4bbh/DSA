class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for element in nums:
            x ^= element
        return x