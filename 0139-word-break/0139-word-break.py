class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        n = len(s)
        keep = set(wordDict)

        def dfs(st = 0):
            if st == n:
                memo[st] = True
                return True

            if st in memo:
                return memo[st]

            for i in range(n):
                subs = s[st : i+1]
                if subs in keep and dfs(i+1):
                    return True
            
            memo[st] = False

            return False
    
        return dfs()