class Solution:
    def check(self, nums: List[int]) -> bool:
        shifted = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if shifted:
                    return False
                shifted = True
        if shifted and nums[0] < nums[-1]:
            return False
        return True