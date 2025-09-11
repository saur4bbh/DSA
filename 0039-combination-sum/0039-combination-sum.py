class Solution:
    def combinationSum(self, arr, target):
        n = len(arr)
        ans = []
        temp = []

        def dfs(summ = 0, i = 0):
            if i == n or summ >= target:
                if summ == target:
                    ans.append(temp[:])
                return

            for j in range(i, n):
                temp.append(arr[j])
                dfs(summ + arr[j], j)
                temp.pop()

            return ans

        return dfs()

        