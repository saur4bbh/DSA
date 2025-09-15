class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = [nums[i] for i in range(n,2*n)]

        i = n-1
        for j in range(2*n-2, -1, -2):
            nums[j] = nums[i]
            i -= 1
        
        i = n-1
        for j in range(2*n-1, 0, -2):
            nums[j] = temp[i]
            i -= 1
        
        return nums
