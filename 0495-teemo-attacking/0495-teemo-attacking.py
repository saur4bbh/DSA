class Solution:
    def findPoisonedDuration(self, time: List[int], d: int) -> int:
        ans = d

        for i in range(1,len(time)):
            if time[i] - time[i-1] < d:
                ans += time[i] - time[i-1]
            else:
                ans += d
        
        return ans