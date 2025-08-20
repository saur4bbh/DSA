class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i,v in enumerate(nums):
            if v != val:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        
        return j