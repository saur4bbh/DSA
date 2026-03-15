class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        r = len(nums) - 1
        l = 0
        ans = 0

        while l < r:
            if nums[r] + nums[l] >= target:
                r -= 1
            else:
                ans += r - l
                l += 1
        
        return ans

