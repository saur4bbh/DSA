class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ele1 = ele2 = ele3 = float('-inf')

        for i in nums:

            if i > ele1:
                ele3, ele2, ele1 = ele2, ele1, i

            elif ele1 > i > ele2:
                ele3, ele2 = ele2, i

            elif ele2 > i > ele3:
                ele3 = i
                
        return ele3 if ele3 != float('-inf') else ele1
