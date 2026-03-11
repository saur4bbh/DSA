class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i,val in zip(index, nums):
            target.insert(i, val)
        
        return target
        