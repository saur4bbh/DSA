class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ss = {}
        for i,val in enumerate(s):
            ss[val] = i
        
        ans = 0
        for i,val in enumerate(t):
            ans += abs(i - ss[val])

        return ans