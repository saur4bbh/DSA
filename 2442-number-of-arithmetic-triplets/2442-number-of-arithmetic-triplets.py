class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set(nums)
        cnt = 0
        for x in nums:
            if x - diff in seen and x + diff in seen:
                cnt += 1
        return cnt