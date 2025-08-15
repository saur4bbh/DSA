class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        a = b = nums[0]
        for i in nums:
            if i!=a!=b:
                if a<b<i or a>b>i: return b
                elif a<i<b or a>i>b: return i
                else: return a
            if b==nums[0] and i!=a: b = i

        return -1


            
