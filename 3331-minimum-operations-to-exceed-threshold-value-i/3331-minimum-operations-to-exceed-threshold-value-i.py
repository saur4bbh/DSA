class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        smaller = 0
        for i in nums:
            if i<k: 
                smaller +=1
        return smaller