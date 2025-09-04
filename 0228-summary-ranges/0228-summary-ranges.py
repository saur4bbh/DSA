class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        i = 0
        while i < len(nums):
            end = i
            while end < len(nums)-1 and nums[end] + 1 == nums[end+1]:
                end += 1

            if i == end:
                ans.append(str(nums[i]))
            else:
                ans.append(str(nums[i]) + '->' + str(nums[end]))
            i = end + 1
        
        return ans




