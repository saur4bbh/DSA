class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = 0
        for i in nums:
            if i <= target:
                end += 1
                if i < target:
                    start += 1
        
        return list(range(start, end))

