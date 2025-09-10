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

            temp.append(arr[i])
            dfs(summ + arr[i], i)
            temp.pop()

            dfs(summ, i + 1)

            return ans

        return dfs()

        