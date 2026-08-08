class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)*2):
            if i >= len(nums):
                ans.append(nums[len(nums)*2 - i - 1])
            else:
                ans.append(nums[i])

        return ans