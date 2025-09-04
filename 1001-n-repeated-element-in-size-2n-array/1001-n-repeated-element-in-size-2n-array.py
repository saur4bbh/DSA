class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        hash = set()
        for i in nums:
            if i in hash:
                return i
            hash.add(i)