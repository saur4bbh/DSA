class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = 0
        suffix = sum(nums)

        for i,val in enumerate(nums):
            prefix += val
            nums[i] = abs(prefix - suffix)
            suffix -= val

        return nums



     