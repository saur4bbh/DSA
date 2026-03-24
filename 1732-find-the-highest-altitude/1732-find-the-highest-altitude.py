class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        curr = 0
        for i in gain:
            curr += i
            highest = max(curr, highest)
        
        return highest