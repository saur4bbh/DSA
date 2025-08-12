class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        a=0
        for i in nums:
            if i%2==0: a+=1
        return [0]*a+[1]*(len(nums)-a)