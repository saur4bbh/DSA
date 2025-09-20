class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        seen = set()
        cnt = 0
        for x in nums:
            if x - diff in seen and x - 2*diff in seen:
                cnt += 1
            seen.add(x)
        return cnt