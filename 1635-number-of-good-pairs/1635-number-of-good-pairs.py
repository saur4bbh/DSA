class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        ans = 0
        for i in d.values():
            ans += i * (i-1) // 2

        return ans
