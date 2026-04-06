class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        x = [0] * 101
        sum = 0

        for i in nums:
            if x[i] == 1:
                x[i] = 2
                sum -= i
            elif x[i] == 0:
                x[i] = 1
                sum += i

        return sum
            
