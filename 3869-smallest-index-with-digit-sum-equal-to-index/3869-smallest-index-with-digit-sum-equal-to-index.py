class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i,val in enumerate(nums):
            k = val
            summ = 0

            while k != 0:
                summ += k%10
                k //= 10

            if summ == i:
                return i

        return -1 
