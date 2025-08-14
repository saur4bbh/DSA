class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = 10**5+1
        for i in nums:
            if abs(i-0)<abs(closest):
                closest = i
            elif abs(i-0)==abs(closest) and closest < i:
                closest = i
        return closest