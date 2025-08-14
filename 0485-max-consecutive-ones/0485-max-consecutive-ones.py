class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        x = 0
        for i in nums:
            if i == 1:
                x += 1
                if x>cnt: cnt = x
            else:
                x = 0
        return cnt