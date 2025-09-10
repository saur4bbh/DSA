class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        temp = []

        def dfs(num, cnt, summ):
            if summ == n and cnt == k:
                ans.append(temp[:])
                return

            if num == 10 or summ > n:
                return
            
            dfs(num+1, cnt, summ)

            temp.append(num)
            dfs(num+1,cnt+1, summ + num)
            temp.pop()

        dfs(1, 0, 0)
        return ans
