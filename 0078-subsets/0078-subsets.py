class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(idx=0, temp = [], ans = [], n = len(nums)):
            if idx == n:
                ans.append(temp[:])
                return

            dfs(idx + 1)

            temp.append(nums[idx])
            dfs(idx + 1)
            temp.pop()

            return ans
        
        return dfs()