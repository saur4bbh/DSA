class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = [0] * len(nums)
        i = 0
        j = len(nums)-1

        for k in range(len(nums)-1,-1,-1):
            if abs(nums[i]) < abs(nums[j]):
                n[k] = nums[j]**2
                j -= 1
            else:
                n[k] = nums[i]**2
                i += 1
        
        return n
