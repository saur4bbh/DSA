class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        shifted = False
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                if shifted:
                    return False
                shifted = True
        return True