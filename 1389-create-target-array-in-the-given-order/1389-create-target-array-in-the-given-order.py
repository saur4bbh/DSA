class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i in zip(index, nums):
            target.insert(i[0], i[1])
        
        return target
        