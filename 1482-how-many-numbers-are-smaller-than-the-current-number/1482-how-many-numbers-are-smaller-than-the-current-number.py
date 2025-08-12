class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}
        
        for a,b in enumerate(sorted(nums)):
            if b not in dict: 
                dict[b]=a

        for i in range(len(nums)):
            nums[i] = dict.get(nums[i])

        return nums