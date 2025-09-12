class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(start = 0):
            if start == n:
                ans.append(nums[:])
                return 
            

            for i in range(start, n):
                nums[start],nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start],nums[i] = nums[i], nums[start]

        backtrack()
        return ans
