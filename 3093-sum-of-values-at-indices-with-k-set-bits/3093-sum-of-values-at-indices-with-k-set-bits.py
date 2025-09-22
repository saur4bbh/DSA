class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i,num in enumerate(nums):
            bit1 = 0
            while i > 0:
                i = i & (i-1)
                bit1 += 1
            if bit1 == k:
                ans += num
        
        return ans