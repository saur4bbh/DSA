class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        track = 0
        for i in s:
            if i == '(':
                track += 1
            elif i == ')':
                track -= 1
            maxi = max(track,maxi)
        
        return maxi