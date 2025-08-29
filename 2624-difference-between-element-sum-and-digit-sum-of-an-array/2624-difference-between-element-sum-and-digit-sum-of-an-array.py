class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele = 0
        digit = 0
        for n in nums:
            ele += n
            while n != 0:
                digit += n % 10
                n //= 10
            
        return abs(ele - digit)