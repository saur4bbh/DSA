class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        temp = []

        def dfs(num, summ):
            if len(temp) == k:
                if summ == n:
                    ans.append(temp[:])
                return

            for i in range(num+1, 10):
                if i > n or summ > n: return
                temp.append(i)
                dfs(i, summ + i)
                temp.pop()

        dfs(0, 0)
        return ans
