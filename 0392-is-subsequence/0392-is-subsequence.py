class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for j in t:
            if i < len(s) and j == s[i]:
                i += 1
        
        return i == len(s)
