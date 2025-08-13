class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n

        def rev(low,high):
            for i in range((high+1-low)//2):
                nums[low+i],nums[high-i] = nums[high-i],nums[low+i]
        
        rev(0,n-1)
        rev(k,n-1)
        rev(0,k-1)
        return nums