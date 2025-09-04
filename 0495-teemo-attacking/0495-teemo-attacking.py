class Solution:
    def findPoisonedDuration(self, time: List[int], d: int) -> int:
        ans = d

        for i in range(1,len(time)):
            ans += min(time[i] - time[i-1], d)
        
        return ans