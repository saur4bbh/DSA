class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        def backtrack(start, temp):
            nonlocal ans
            ans += temp
            
            for i in range(start, n):
                backtrack(i+1, temp ^ nums[i])
        
        backtrack(0, 0)
        return ans

