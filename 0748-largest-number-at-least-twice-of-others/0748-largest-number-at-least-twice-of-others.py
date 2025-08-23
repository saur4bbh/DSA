class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        big1 = big2 = float('-inf')
        idx = 0
        for i,val in enumerate(nums):
            if val > big1:
                big2, big1 = big1, val
                idx = i
            elif val> big2:
                big2 = val

        return idx if big1 >= 2*big2 else -1