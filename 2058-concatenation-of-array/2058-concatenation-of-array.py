class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.extend([None]*n)
        nums[n:] = nums[:n]
        return nums