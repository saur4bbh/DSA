class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        a = 51
        for i in range(len(nums)//2):
            if (nums[i]+nums[~i])/2 < a:
                a = (nums[i]+nums[~i])/2
        return a