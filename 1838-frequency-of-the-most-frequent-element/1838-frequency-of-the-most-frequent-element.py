class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        i = j = 0
        freq = calc = 0

        while j < len(nums):
            if calc <= k:
                freq = max(freq, j - i + 1)
                j += 1
                if j < len(nums): calc += nums[i] - nums[j]
            else:
                calc -= (j - i) * (nums[i] - nums[i+1])
                i += 1
        
        return freq