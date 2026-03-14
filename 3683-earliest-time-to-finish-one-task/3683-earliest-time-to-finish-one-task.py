class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = 10**3
        for i in tasks:
            time = i[0] + i[1]
            ans = min(ans, time)
        
        return ans