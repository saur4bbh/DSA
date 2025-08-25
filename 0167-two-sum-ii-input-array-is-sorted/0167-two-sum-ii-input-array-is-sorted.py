class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        while i<j:
            summ = nums[i] + nums[j]
            if summ > target:
                j -= 1
            elif summ < target:
                i += 1
            else:
                return[i+1,j+1]