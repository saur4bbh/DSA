class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        k = 1

        while k < len(nums):
            if nums[j] < nums[k]:
                j += 1
                nums[j] = nums[k]
            k += 1
        
        return j+1