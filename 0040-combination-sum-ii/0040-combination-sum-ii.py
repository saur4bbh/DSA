class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        temp = []

        def dfs(i=0, summ = 0):
            if i == n or summ >=target:
                if summ == target:
                    ans.append(temp[:])
                return 
            
            temp.append(candidates[i])
            dfs(i+1, summ + candidates[i])
            temp.pop()

            while i < n-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, summ)
        

        dfs()
        return ans
