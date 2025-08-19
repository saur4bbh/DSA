class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        length = 0

        for ele in sett:
            if ele-1 not in sett:
                i = ele
                count = 1
                while i+1 in sett:
                    i += 1
                    count += 1
                length = max(length,count)
        
        return length