class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ele = 0
        for i in nums:
            if cnt == 0:
                cnt,ele = 1,i
            elif ele == i: cnt += 1
            else: cnt -= 1
        return ele