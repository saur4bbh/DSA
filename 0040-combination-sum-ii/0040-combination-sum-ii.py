class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        temp = []

        def dfs(start=0, summ = 0):
            if start == n or summ >=target:
                if summ == target:
                    ans.append(temp[:])
                return 
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:   #optimisation since sorted
                    break
                temp.append(candidates[i])
                dfs(i+1, summ + candidates[i])
                temp.pop()      

        dfs()
        return ans
