class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        b = -101

        for i in range(len(nums)):
            if b!=nums[i]:
                b = nums[i]
                nums[a]=b
                a+=1
        
        return a