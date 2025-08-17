class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        val = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]: 
                val = i
                break
        
        if val != -1:
            for i in range(len(nums)-1,val,-1):
                if nums[i]>nums[val]:
                    nums[val],nums[i] = nums[i],nums[val]
                    break

        i = val + 1
        j = len(nums)-1

        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            j -= 1
            i += 1
