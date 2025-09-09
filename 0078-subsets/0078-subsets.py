class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        temp = []

        def dfs(idx):
            if idx == n:
                ans.append(temp[:])
                return

            dfs(idx + 1)

            temp.append(nums[idx])
            dfs(idx + 1)
            temp.pop()
        
        dfs(0)
        return ans