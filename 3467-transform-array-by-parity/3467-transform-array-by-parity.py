class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] % 2 == 1:
                nums[i] = nums[j]
                nums[j] = 1
                j -= 1
            else:
                nums[i] = 0
                i += 1
        
        return nums