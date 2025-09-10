class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        temp = []

        def dfs(start):
            ans.append(temp[:])

            for i in range(start, n):
                if i > start and nums[i-1] == nums[i]:
                    continue
                temp.append(nums[i])
                dfs(i+1)
                temp.pop()

        dfs(0)
        return ans


